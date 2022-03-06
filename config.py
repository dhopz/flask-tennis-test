"""Flask configuration variables."""
from os import path
from dotenv import load_dotenv
import os

load_dotenv()

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    """Set Flask configuration from .env file."""

    
    # PostgreSQL Database credentials loaded from the .env file
    DATABASE = os.getenv('DATABASE')
    DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
    DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')

    # Database
    SQLALCHEMY_DATABASE_URI = "postgresql://"+DATABASE_USERNAME+":password@localhost/tennis"
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


