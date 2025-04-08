import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DEBUG = os.getenv("DEBUG", "False") == "True"
    OFFLINE_MODE = os.getenv("OFFLINE_MODE", "False") == "True"
    SECRET_KEY = os.getenv("SECRET_KEY", "default-secret-key")
