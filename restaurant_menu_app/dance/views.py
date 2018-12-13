import os
from flask import url_for
from flask_dance.contrib.github import make_github_blueprint, github
from flask_dance.consumer.backend.sqla import SQLAlchemyBackend
from flask_login import current_user
from restaurant_menu_app import db
from restaurant_menu_app.models import OAuth

blueprint = make_github_blueprint(client_id=os.environ.get("GH_CLIENT_ID"),
                                  client_secret=os.environ.get("GH_CLIENT_SECRET"))

blueprint.backend = SQLAlchemyBackend(OAuth, db.session, user=current_user)


