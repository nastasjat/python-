# search images in gif format via GIPHY API
# (requires API key from https://developers.giphy.com/dashboard/)

import requests
import os
from dotenv import load_dotenv


def get_gifs():
    load_dotenv()
    api_key = os.getenv("MY_GIPHY_API_KEY")

    GIPHY_URL = "https://api.giphy.com/v1/gifs/search"

    search = input("Please enter a word:")
    resp = requests.get(GIPHY_URL, params={"api_key": api_key, "q": search})
    content = resp.json()

    links = [gif["images"]["fixed_height"]["url"] for gif in content["data"]]

    print("GIFs based on your search: ")
    for gif in links:
        print(gif)


get_gifs()
