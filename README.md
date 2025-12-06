# JobMatch AI 🔍✨

An intelligent job matching system that analyzes resumes and matches them with the most suitable job postings using AI.

## Features

- 📄 **Resume Analysis**: Extract and analyze text from PDF resumes
- 🤖 **AI-Powered Matching**: Uses Google's Gemini AI to match resumes with job descriptions
- 🎯 **Smart Scoring**: Provides a suitability score (0-100) for each job match
- 💡 **Actionable Insights**: Get detailed reasons for matches and preparation tips
- ⚡ **Fast Processing**: Optimized for quick analysis of multiple job postings

## Prerequisites

- Python 3.8+
- Google AI API key
- Apify API key (for job scraping, if needed)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/jobmatch-ai.git
   cd jobmatch-ai
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a [.env](.env) file and add your API keys:
   ```
   GOOGLE_AI_API=your_google_ai_api_key
   APIFY_API_KEY=your_apify_api_key
   ```

## Usage

1. Start the Flask server:

   ```bash
   python app.py
   ```

2. Send a POST request to `/extract` with a PDF resume:
   ```bash
   curl -X POST -F "file=@/path/to/your/resume.pdf" http://localhost:3000/extract
   ```

## API Endpoints

### POST /extract

Upload a PDF resume and get job matches.

**Request:**

- Method: POST
- Content-Type: multipart/form-data
- Body: `file` (PDF file)

**Response:**

```json
[
   {
    "job_title": "Frontend Software Engineer (React, TypeScript or JavaScript)",
    "score": 60,
    "match_reason": "The candidate has strong proficiency in React, JavaScript, and TypeScript, essential for this front-end role. Critically, their robust Python programming skills and hands-on experience in machine learning and AI (TensorFlow, PyTorch, Generative AI, Nillion AI Prize) make them an excellent match for supporting AI labs and developing coding benchmarks, which is the core focus. While the stated 3-10 years of experience is a hurdle, the depth of technical skills and relevance of AI projects are highly compelling, especially for a contract/part-time role that may value specific technical expertise.",
    "prepare": "Emphasize how their AI/ML knowledge allows them to understand and contribute to coding benchmarks for AI systems. Highlight any personal experience with code quality, testing (e.g., unit tests in projects), and debugging. Be ready to discuss the technical aspects of their AI projects and how they would approach curating issues and solutions for AI-related coding tasks."
  },
]
```

## Project Structure

```
.
├── app.py              # Main Flask application
├── data.json           # Sample job postings
├── requirements.txt    # Python dependencies
├── .env                # Environment variables
└── README.md           # This file
```

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Google AI for the powerful Gemini model
- Flask for the lightweight web framework
- PyPDF2 for PDF text extraction

```

### Additional Recommendations:

1. Create a `requirements.txt` file with the following content:
```

flask==2.3.3
flask-cors==4.0.0
PyPDF2==3.0.1
python-dotenv==1.0.0
google-generativeai==0.3.0
apify-client==1.2.2

```

2. Create a `.env` file:
```

GOOGLE_AI_API=your_google_ai_api_key_here
APIFY_API_KEY=your_apify_api_key_here

```

```
