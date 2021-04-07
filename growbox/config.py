import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "key_for_development")
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///site.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False