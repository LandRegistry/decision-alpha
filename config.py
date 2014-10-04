import os

class Config(object):
    DEBUG = False
    CASEWORK_URL = os.environ['CASEWORK_URL']
    CHECK_URL = os.environ['CHECK_URL']

class DevelopmentConfig(Config):
    DEBUG = True

class TestConfig(DevelopmentConfig):
    TESTING = True
