import os
class Config:
    SECRET_KEY='thisismysupersecretkey'
    
    MAIL_SERVER : 'smtp.googlemail.com'
    MAIL_PORT : 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME : os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD : os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER : os.environ.get('MAIL_USERNAME')

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://postgres:12345678@localhost/elevator_pitch'
    DEBUG=True
   

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('REMOTE_DATABASE_URL')

configuration_options ={
    'development': DevConfig,
    'production': ProdConfig
}
