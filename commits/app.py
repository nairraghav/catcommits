import requests
import requests_cache
from commits.models.cat_commit import CatCommit
from flask import Flask, render_template, request

app = Flask(__name__)

requests_cache.install_cache('github_cache', backend='sqlite', expire_after=10800)


@app.route('/', methods=["GET"])
def home():
    page_number = int(request.args.get("page_number", default=1))
    if 0 < page_number < 35:  # we are not allowed search beyond 1000 results
        github_cat_search_url = f"https://api.github.com/search/commits?q=cat&page={page_number}"
        headers = {"Accept": "application/vnd.github.cloak-preview"}
        cat_search_response = requests.get(url=github_cat_search_url, headers=headers)
        cat_commits = []
        items = cat_search_response.json().get('items')
        if items:
            print(f"{page_number} has items!")
            for item in items:
                cat_commits.append(CatCommit(item))
            return render_template('home.html', commits=cat_commits, page_number=page_number, no_kitties=False)
    return render_template('home.html', page_number=page_number, no_kitties=True)
