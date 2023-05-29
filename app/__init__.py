from flask import Flask
from .api.employee import employee_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(employee_bp, url_prefix='/api')
    return app
