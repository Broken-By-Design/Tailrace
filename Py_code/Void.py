# THIS IS A VOID FILE
# PLEASE IGNORE IT!

"""
import os

import requests
from dotenv import load_dotenv

load_dotenv()
VRCHAT_TOKEN = os.getenv("VRCHAT_TOKEN")

if not VRCHAT_TOKEN:
    print("YO! Your VRCHAT_TOKEN is empty. CHECK YOUR .env FILE")
    raise SystemExit(1)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/111.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Referer": "https://vrchat.com/",
}

url = "https://api.vrchat.cloud/api/1/users"

try:
    resp = requests.get(
        url, headers=headers, cookies={"auth": VRCHAT_TOKEN}, timeout=10
    )
    resp.raise_for_status()
    # use resp.json() only if response is JSON
    print("Success; status:", resp.status_code)
    print(resp.text[:1000])  # preview only, don't print token or full sensitive data
except requests.HTTPError as e:
    print("HTTP error:", e)
    if e.response is not None:
        print("Status:", e.response.status_code)
        print("Body preview:", e.response.text[:500])
except requests.RequestException as e:
    print("Request failed:", e)
"""
