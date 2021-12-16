import os
class Config(object):
    DEBUG=False
    TESTING=False
    CSRF_ENABLED=True
    MONGODB_URI=os.environ.get('MONGODB_DATABASE_URI')
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))  
    # APPLICATION_ROOT="/auth"


class ProductionConfig(Config):
    DEBUG=False
    SECRET_KEY=os.environ.get('SECRET_KEY')

class DevelopmentConfig(Config):
    ENV = "development"
    MONGODB_URI='mongodb://localhost:27017'
    DEVELOPMENT = True
    SECRET_KEY = "secret_for_test_environment"