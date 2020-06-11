# Cat Commits
This repository contains code for a simple Flask app that uses the GitHub API to search commits containing the word cat.

## Custom Configuration
If you want to stand up your own version of this but for a different search type, you can do so quite easily! After
cloning the repo, update the `commits/app.py` to remove `cat` and replace it with whatever keyword you would like. 
The only other changes you would need to make are for the background image within the `commits/templates/home.html`
file

Do note that we are using GitHub's API (non authenticated) so we are limited to 10 requests per minute.


## Website
This is hosted [here](http://cat-commits.raghav-nair.com) via Heroku & Google Domains

