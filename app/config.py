import os
class Config:
    SECRET_KEY='thisismysupersecretkey'
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    MAIL_SERVER : 'smtp.googlemail.com'
    MAIL_PORT : 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME : os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD : os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER : os.environ.get('MAIL_USERNAME')

class DevConfig(Config):
    DEBUG=True


class ProdConfig(Config):
    DEBUG=False
    

configuration_options ={
    'development': DevConfig,
    'production': ProdConfig
}
