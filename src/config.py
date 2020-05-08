from settings import USER_DB, PASSWORD, DATABASE, PORT


class Config(object):
    """
    Class to set config
    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    """
    Class to config application for production
    """
    SQLALCHEMY_DATABASE_URI = f"postgresql://{USER_DB}:{PASSWORD}@{DATABASE}:{PORT}/gloria"
