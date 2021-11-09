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
    SQLALCHEMY_DATABASE_URI = 'postgres://vphupjjouxbchm:405e9885277306ea2a33321740801ee7a20f15e7d46524754f68e896f27fb4f6@ec2-54-146-84-101.compute-1.amazonaws.com:5432/dd4o6grtfa94e'


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
