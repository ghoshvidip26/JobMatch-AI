from apify_client import ApifyClient
from dotenv import load_dotenv
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from PyPDF2 import PdfReader
import collections
import json
from pydantic import BaseModel
collections.Iterable = collections.abc.Iterable

import google.generativeai as genai

load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GOOGLE_AI_API"))
apify_client = ApifyClient(os.getenv("APIFY_API_KEY"))

app = Flask(__name__)
CORS(app)

class Document(BaseModel):
    page_content: str
    metadata: dict


@app.route("/extract", methods=["POST"])
def extract():
    if "file" not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files["file"]
    try:
        # Read PDF
        reader = PdfReader(file)
        text = "".join(page.extract_text() + "\n" for page in reader.pages)
        resume_text = text[:3000]  # Limit length to speed up

        # Load jobs
        with open("data.json", "r") as f:
            jobs = json.load(f)

        # Prepare prompt
        prompt = f"""
You are an expert job suitability analyzer.

Resume:
{resume_text}

Jobs:
{json.dumps(jobs)}

For each job, return ONLY a JSON array with:
[
  {{
    "job_title": "<job title>",
    "score": <0-100>,
    "match_reason": "<string explaining suitability>",
    "prepare": "<string advising what to prepare>"
  }},
  ...
]

Return valid JSON only. Remove any leading text like 'json' or markdown formatting.
"""

        # Initialize the model
        model = genai.GenerativeModel("gemini-2.5-flash")

        # Generate response
        response = model.generate_content(prompt)
        response_text = response.text.strip()

        # Remove leading "json" or markdown symbols
        for prefix in ["json", "```json", "```"]:
            if response_text.lower().startswith(prefix):
                response_text = response_text[len(prefix):].strip()

        # Parse JSON safely
        try:
            parsed_results = json.loads(response_text)
        except Exception as e:
            return jsonify({"error": f"Failed to parse JSON: {str(e)}", "raw": response_text}), 500

        # Filter suitable jobs (score > 60)
        suitable_jobs = [job for job in parsed_results if job.get("score", 0) > 60]

        return jsonify({
            "all_jobs": parsed_results,
            "suitable_jobs": suitable_jobs
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=3000)