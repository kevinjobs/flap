import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    @staticmethod
    def init_app(app):
        pass


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URL",
                                             'sqlite:///' + os.path.join(basedir, 'data.dev.sqlite'))


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URL",
                                             'sqlite:///' + os.path.join(basedir, 'data.dev.sqlite'))


class ProdConfig(Config):
    pass


config = {
    'development': DevConfig,
    'testing': TestConfig,
    'production': ProdConfig,
    'default': DevConfig,
}