import os

class Config:
    """
    General configuration class
    """
    SECRET_KEY = 'SECRET_KEY'
    
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    
    # Email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'robbin.githimbo@student.moringaschool.com'
    MAIL_PASSWORD = 'Shizzle27!'


class ProdConfig(Config):
    """
    Production configuration class
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:access@localhost/pitches_test'



class DevConfig(Config):
    """
    Development configuration class
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:access@localhost/pitches'
    DEBUG = True
    



config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}
