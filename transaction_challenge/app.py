import logging
from flask import Flask

def create_app() -> Flask:
    app = Flask("transaction_challenge")
    
    from transaction_challenge.api.api import api as api_blueprint
    
    app.register_blueprint(api_blueprint)
    return app

def configure_logging() -> None:
    logging.basicConfig(level=logging.INFO)