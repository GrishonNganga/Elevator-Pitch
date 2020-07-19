import os
class Config:
    SECRET_KEY='thisismysupersecretkey'
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://postgres:12345678@localhost/elevator_pitch'

class DevConfig(Config):
    DEBUG=True
    MAIL_SERVER : 'smtp.googlemail.com'
    MAIL_PORT : 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME : os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD : os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER : os.environ.get('MAIL_USERNAME')

class ProdConfig(Config):
    pass

configuration_options ={
    'development': DevConfig,
    'producrion': ProdConfig
}
