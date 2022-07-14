import os
import json
import requests
from dotenv import load_dotenv
load_dotenv()

ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY")

def search_images(query, page):
    api_endpoint = "https://api.unsplash.com/search/photos"
    request_endpoint = api_endpoint + "?page=" + str(page) + "&query=" + str(query) + "&client_id=" + str(ACCESS_KEY)
    response = requests.get(request_endpoint)
    return json.loads(response.text)

def get_random_image(query):
    api_endpoint = "https://api.unsplash.com/photos/random"
    request_endpoint = api_endpoint + "?query=" + str(query) + "&client_id=" + str(ACCESS_KEY)
    response = requests.get(request_endpoint)
    return json.loads(response.text)