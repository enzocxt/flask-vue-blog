from flask import Flask
from flask_cors import CORS
from config import Config


# use app factory to create Flask app
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # 前端地址是 localhost:8080，而后端是 5000
    # 所以前端发来的 ajax 请求属于跨域请求
    # enable CORS
    CORS(app)

    # register blueprint
    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app
