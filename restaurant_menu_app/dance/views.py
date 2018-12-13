import os
from flask import url_for
from flask_dance.contrib.github import make_github_blueprint, github

blueprint = make_github_blueprint(client_id=os.environ.get("GH_CLIENT_ID"),
                                  client_secret=os.environ.get("GH_CLIENT_SECRET"))




