import os

USER_DB = os.getenv("USER_DB", "admin")
PASSWORD = os.getenv("PASSWORD", "admin")
DATABASE = os.getenv("DATABASE", "localhost")
PORT = os.getenv("PORT", "5432")