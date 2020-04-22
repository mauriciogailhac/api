from settings import USER_DB, PASSWORD, DATABASE, PORT


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = f"postgresql://{USER_DB}:{PASSWORD}@{DATABASE}:{PORT}/gloria"
