import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    APP_ENV = os.getenv("APP_ENV")
    DB_USER = os.getenv("MARIADB_USER")
    DB_DATABASE = os.getenv("MARIADB_DATABASE")
    DB_PASSWORD = os.getenv("MARIADB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
