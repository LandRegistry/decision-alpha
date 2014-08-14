import os

class Config(object):
    CASEWORK_URL = os.environ.get('CASEWORK_URL') 
    CHECK_URL = os.environ.get('CHECK_URL')
    

class DevelopmentConfig(Config):
    DEBUG = True

class TestConfig(DevelopmentConfig):
    TESTING = True

class DockerConfig(Config):
    DEBUG = True