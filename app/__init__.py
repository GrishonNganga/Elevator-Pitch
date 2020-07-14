from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from .config import configuration_options
bootstrap = Bootstrap()
db = SQLAlchemy()
def create_app(configuration):
    app = Flask(__name__)
    app.config.from_object(configuration_options[configuration])

    bootstrap.init_app(app)
    db.init_app(app)
    
    from .auth.views import auth as auth_blueprint
    from .views import app as app_blueprint
    from .categories.views import category as category_blueprint

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(app_blueprint)
    app.register_blueprint(category_blueprint)
    
    return app