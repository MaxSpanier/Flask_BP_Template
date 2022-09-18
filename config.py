class Config(object):
    TESTING = False

class ProductionConfig(Config):
    # Save secret key somewhere safe

class DevelopmentConfig(Config):
    TESTING = True
    SECRET_KEY = '\xc5\xde=\xf4Q\x08)\xd0\xfcT\x1d*D\x1aQ\xd3\xb4\x80s\x8b\xc4R\x08\xd8'
