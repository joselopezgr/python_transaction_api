import pytest

from transaction_challenge.domain.service.Event_handler import EventHandler
from transaction_challenge.domain.dto.clientTransactionDto import ClientTransactionDto

@pytest.fixture(autouse=True)
def reset_transactions():
    EventHandler.depositTransactions = []
    EventHandler.withdrawalTransactions = []

def test_handle_deposit_event():
    event_data = ClientTransactionDto(type="deposit", amount="150", time=10, user_id=1)
    response = EventHandler.handle_event(event_data)
    assert response['alert']
    assert 123 in response['alert_codes']

def test_handle_withdrawal_event():
    event_data = ClientTransactionDto(type="withdrawal", amount="200", time=10, user_id=1)
    response = EventHandler.handle_event(event_data)
    assert response['alert']
    assert 1100 in response['alert_codes']