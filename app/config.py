import os
class Config:
    SECRET_KEY='thisismysupersecretkey'
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://postgres:12345678@localhost/elevator_pitch'

class DevConfig(Config):
    DEBUG=True
    MAIL_SERVER : 'smtp.googlemail.com'
    MAIL_PORT : 587
    MAIL_USE_TLS = True
    MAIL_USERNAME : os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD : os.environ.get('MAIL_PASSWORD')

class ProdConfig(Config):
    pass

configuration_options ={
    'development': DevConfig,
    'producrion': ProdConfig
}
