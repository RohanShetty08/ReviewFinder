from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import json
from googlesearch import search
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


def tik_tok_scrape(search_term):
    return






def video_urls(search_term):
    try:
        # Perform Google search and get first four results
        search_results = search("tiktok " + search_term + " review",
                                num=12, stop=12, pause=2)

        # Filter out URLs that are Reddit pages
        tiktok_pages = [url for url in search_results if "tiktok.com" in url and "/video" in url]
        video_ids = []

        for page in tiktok_pages:
            url_parts = page.split("/")
            video_id = url_parts[-1]  # Assuming the last part of the URL is the video ID
            video_ids.append(video_id)
        return video_ids
    except Exception as e:
        print("An error occurred:", str(e))
        return None


@app.route('/searchQueries', methods=['POST'])
def handle_search_query():
    data = request.json
    search_term = data['searchQuery']
    urls = video_urls(search_term)
    return jsonify({'videoUrls': urls})


def get_reddit_pages(query):
    try:
        # Perform Google search and get first four results
        search_results = search(query + "review reddit",
                                num=15, stop=15, pause=2)

        # Filter out URLs that are Reddit pages
        reddit_pages = [url for url in search_results if "reddit.com" in url]
        return reddit_pages
    except Exception as e:
        print("An error occurred:", str(e))
        return None

# Add this function to your existing Flask app


@app.route('/TikTokPages', methods=['POST'])
def handle_TikTok_pages():
    data = request.json
    search_term = data['searchQuery']
    search_type = data['searchType']
    tiktok_pages = video_urls(search_term + " "+ search_type)
    print("TIKTOKPAGES", tiktok_pages)
    return jsonify({'TikTok_data': tiktok_pages})


@app.route('/redditPages', methods=['POST'])
def handle_reddit_pages():
    data = request.json
    search_term = data['searchQuery']
    search_type = data['searchType']
    reddit_pages = get_reddit_pages(search_term + " "+ search_type)
    return jsonify({'redditPages': reddit_pages})


if __name__ == '__main__':
    app.run(debug=True)
