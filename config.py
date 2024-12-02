import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

class Config:
    """Base configuration class."""
    API_TITLE = "Ecommerce"
    API_VERSION = "v1"
    OPENAPI_VERSION = "3.0.3"
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")


    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", 'sqlite:///ecommerce.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ENV = os.getenv("FLASK_ENV", "development")

    # No SSL settings required for SQLite
    SQLALCHEMY_ENGINE_OPTIONS = {}

   
