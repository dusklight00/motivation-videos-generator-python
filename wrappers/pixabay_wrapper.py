import os
import requests
import json
from urllib.parse import quote
from dotenv import load_dotenv
from pprint import pprint
load_dotenv()

API_KEY = os.getenv("PIXABAY_API_KEY")

def search_videos(query):
    url = f'https://pixabay.com/api/videos/?key={API_KEY}&q={quote(query.encode("utf-8"))}&pretty=true'
    response = requests.get(url)
    return json.loads(response.text)

def search_high_quality_videos(query):
    results = search_videos(query)
    high_quality_video_collection = [ hit["videos"]["large"] for hit in results["hits"] if hit["videos"]["large"]["url"] != "" ]
    return high_quality_video_collection