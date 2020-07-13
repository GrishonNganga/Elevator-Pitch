class Config:
    SECRET_KEY='thisismysupersecretkey'
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://postgres:12345678@localhost/elevator_pitch'

class DevConfig(Config):
    DEBUG=True

class ProdConfig(Config):
    pass

configuration_options ={
    'development': DevConfig,
    'producrion': ProdConfig
}
