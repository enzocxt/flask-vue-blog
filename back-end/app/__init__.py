from flask import Flask
from config import Config


# use app factory to create Flask app
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # register blueprint
    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app
