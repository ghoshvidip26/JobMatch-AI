from __future__ import annotations
import json
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from httpx import AsyncClient

with open('data.json') as f: 
    d = json.load(f)
    print(d)


# Prepare the Actor input
run_input = {
    "position": "web developer",
    "country": "US",
    "location": "San Francisco",
    "maxItems": 50,
    "parseCompanyDetails": False,
    "saveOnlyUniqueItems": True,
    "followApplyRedirects": False,
    "startUrls": None,
    "maxItemsPerSearch": None,
}

# Run the Actor and wait for it to finish
run = client.actor("hMvNSpz3JnHgl5jkh").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset (if there are any)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)