import os

class Config:
    SECRET_KEY = os.environ.get('RESTAURANT_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('RESTAURANT_DB')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
