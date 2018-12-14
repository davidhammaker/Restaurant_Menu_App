import os
from flask import flash
from sqlalchemy.orm.exc import NoResultFound
from flask_dance.contrib.github import make_github_blueprint, github
from flask_dance.consumer.backend.sqla import SQLAlchemyBackend
from flask_dance.consumer import oauth_authorized, oauth_error
from flask_login import current_user, login_user, login_required, logout_user
from restaurant_menu_app import db
from restaurant_menu_app.models import OAuth, User

blueprint = make_github_blueprint(client_id=os.environ.get("GH_CLIENT_ID"),
                                  client_secret=os.environ.get("GH_CLIENT_SECRET"))

blueprint.backend = SQLAlchemyBackend(OAuth, db.session, user=current_user)


@oauth_authorized.connect_via(blueprint)
def github_logged_in(blueprint, token):
    if not token:
        flash("Failed to log in with GitHub.", "bad")
        return False

    resp = blueprint.session.get('/user')
    if not resp.ok:
        flash("Failed to fetch user info from GitHub", "bad")
        return False

    github_info = resp.json()
    github_user_id = str(github_info["id"])

    query = OAuth.query.filter_by(provider=blueprint.name, provider_user_id=github_user_id, token=token)
    try:
        oauth = query.one()
    except NoResultFound:
        oauth = OAuth(provider=blueprint.name, provider_user_id=github_user_id, token=token)

    if oauth.user:
        login_user(oauth.user)
        flash("Successfully signed in with GitHub!", "good")
    else:
        user = User(email=github_info["email"], name=github_info["name"], username=github_info["login"])
        oauth.user = user
        db.session.add_all([user, oauth])
        db.session.commit()
        login_user(user)
        flash("Successfully signed in with GitHub!", "good")
    return False


@oauth_error.connect_via(blueprint)
def github_error(blueprint, error, error_description=None, error_uri=None):
    flash(f"OAuth error from {blueprint.name}! error={error} description={error_description} uri={error_uri}", "bad")
