import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///default.db')
    API_KEY = os.getenv('API_KEY', 'YourDefaultAPIKey')
    DEBUG = os.getenv('DEBUG', 'False').lower() in ('true', '1', 't')