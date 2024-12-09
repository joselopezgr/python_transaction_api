import pytest
from flask import Flask
from flask.testing import FlaskClient
from transaction_challenge.app import create_app

@pytest.fixture
def app() -> Flask:
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    return app

@pytest.fixture
def client(app: Flask) -> FlaskClient:
    return app.test_client()

@pytest.fixture(autouse=True)
def reset_transactions():
    from transaction_challenge.domain.service.Event_handler import EventHandler
    EventHandler.depositTransactions = []
    EventHandler.withdrawalTransactions = []