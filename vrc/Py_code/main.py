import json
import os
import urllib

import requests
from dotenv import load_dotenv


def get_env():  # THIS IS FLAWED! WHAT IF YOU NEED MULTIPLE THINGS FROM THE .env?!

    load_dotenv()

    VRCHAT_TOKEN = os.getenv("VRCHAT_TOKEN")

    return VRCHAT_TOKEN


vrchat_token = get_env()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}

url = "https://api.vrchat.cloud/api/1/users"

# THIS DOES NOT RETURN ACTIVE PLAYERS, I EITHER NEED TO FIGURE OUT THE VRCHAT API IF THIS EVEN EXISTS! OR I NEED TO USE ActivePlayer.io, SteamDB and Tracker.gg
# ActivePlayer.io is best for all platforms, SteamDB or just the steam API is best for pulling steam!
# Can do ActivePlayer.io count - SteamDB = Other patforms (quest and pico...etc...)

if not vrchat_token:
    print("YO! Your VECHAT_TOKEN is empty. CHECK YOUR DAMN .env FILE")
else:
    response = requests.request(
        "GET", url, cookies={"auth": vrchat_token}, headers=headers
    )

    print(response.text)
