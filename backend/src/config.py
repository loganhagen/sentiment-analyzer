class Config:
        TESTING = False

class DevelopmentConfig(Config):
    pass

class TestingConfig(Config):
    Testing = True

class ProductionConfig(Config):
    pass