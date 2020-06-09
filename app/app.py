import requests
import requests_cache
from app.cat_commit import CatCommit
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

requests_cache.install_cache('github_cache', backend='sqlite', expire_after=180)


@app.route('/', methods=["GET"])
def home():
    github_cat_search_url = "https://api.github.com/search/commits?q=cat"
    headers = {"Accept": "application/vnd.github.cloak-preview"}
    cat_search_response = requests.get(url=github_cat_search_url, headers=headers)
    cat_commits = []
    for item in cat_search_response.json()['items']:
        cat_commit = CatCommit(item)
        if cat_commit.good_commit:
            cat_commits.append(cat_commit)
    return render_template('home.html', commits=cat_commits)
