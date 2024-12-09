import pytest

from transaction_challenge.domain.service.Event_handler import EventHandler
from transaction_challenge.domain.dto.clientTransactionDto import ClientTransactionDto

@pytest.fixture(autouse=True)
def reset_transactions():
    EventHandler.depositTransactions = []
    EventHandler.withdrawalTransactions = []

# 1. TESTS FOR THE MORE 100 WITHDRAWALS CHECK 
def test_handle_withdrawal_event():
    event_data = ClientTransactionDto(type="withdrawal", amount="200", time=10, user_id=1)
    response = EventHandler.handle_event(event_data)
    
    assert response['alert']
    assert 1100 in response['alert_codes']
    
def test_handle_withdrawal_event_unhappy():
    event_data = ClientTransactionDto(type="withdrawal", amount="100", time=10, user_id=1)
    response = EventHandler.handle_event(event_data)
    
    assert not response['alert']
    assert 1100 not in response['alert_codes']

# 2. TESTS FOR THE CONSECUTIVE WITHDRAWALS CHECK 
def test_handle_deposit_event():
    event_data_1 = ClientTransactionDto(type="withdrawal", amount="20", time=10, user_id=1)
    event_data_2 = ClientTransactionDto(type="withdrawal", amount="20", time=10, user_id=1)
    event_data_3 = ClientTransactionDto(type="withdrawal", amount="20", time=10, user_id=1)
    EventHandler.handle_event(event_data_1)
    EventHandler.handle_event(event_data_2)
    response = EventHandler.handle_event(event_data_3)
    
    assert response['alert']
    assert 30 in response['alert_codes']

def test_handle_consecutive_withdrawals_unhappy():
    event_data_1 = ClientTransactionDto(type="withdrawal", amount="20", time=10, user_id=1)
    event_data_2 = ClientTransactionDto(type="withdrawal", amount="20", time=10, user_id=1)
    event_data_3 = ClientTransactionDto(type="deposit", amount="20", time=10, user_id=1)
    EventHandler.handle_event(event_data_1)
    EventHandler.handle_event(event_data_2)
    response = EventHandler.handle_event(event_data_3)

    assert not response['alert']
    assert 30 not in response['alert_codes']

# 3. TESTS FOR THE 3 CONSECUTIVE DEPOSITS CHECK 
def test_handle_3_consecutive_deposit_event():
    event_data_1 = ClientTransactionDto(type="deposit", amount="40", time=0, user_id=1)
    event_data_2 = ClientTransactionDto(type="deposit", amount="45", time=20, user_id=1)
    event_data_3 = ClientTransactionDto(type="deposit", amount="50", time=50, user_id=1) 
    EventHandler.handle_event(event_data_1)
    EventHandler.handle_event(event_data_2)
    response = EventHandler.handle_event(event_data_3)
    
    assert response['alert']
    assert 300 in response['alert_codes']

def test_handle_3_consecutive_deposit_event_unhappy():
    event_data_1 = ClientTransactionDto(type="deposit", amount="40", time=0, user_id=1)
    event_data_2 = ClientTransactionDto(type="deposit", amount="45", time=20, user_id=1)
    event_data_3 = ClientTransactionDto(type="withdrawal", amount="50", time=50, user_id=1)
    EventHandler.handle_event(event_data_1)
    EventHandler.handle_event(event_data_2)
    response = EventHandler.handle_event(event_data_3)

    assert not response['alert']
    assert 300 not in response['alert_codes']

# 4. TESTS FOR THE 30s DEPOSITS MORE THAN 200 CHECK 
def test_handle_30s_consecutive_event():
    event_data_1 = ClientTransactionDto(type="deposit", amount="100", time=0, user_id=1)
    event_data_2 = ClientTransactionDto(type="deposit", amount="100", time=10, user_id=1)
    event_data_3 = ClientTransactionDto(type="deposit", amount="50", time=20, user_id=1)
    EventHandler.handle_event(event_data_1)
    EventHandler.handle_event(event_data_2)
    response = EventHandler.handle_event(event_data_3)
    assert response['alert']
    assert 123 in response['alert_codes']
    
def test_handle_30s_consecutive_event_different_times():
    event_data_1 = ClientTransactionDto(type="deposit", amount="100", time=50, user_id=1)
    event_data_2 = ClientTransactionDto(type="deposit", amount="100", time=60, user_id=1)
    event_data_3 = ClientTransactionDto(type="deposit", amount="50", time=80, user_id=1)
    EventHandler.handle_event(event_data_1)
    EventHandler.handle_event(event_data_2)
    response = EventHandler.handle_event(event_data_3)
    assert response['alert']
    assert 123 in response['alert_codes']

def test_handle_30s_consecutive_event_unhappy():
    event_data_1 = ClientTransactionDto(type="deposit", amount="100", time=0, user_id=1)
    event_data_2 = ClientTransactionDto(type="deposit", amount="100", time=40, user_id=1)
    event_data_3 = ClientTransactionDto(type="deposit", amount="50", time=80, user_id=1)
    EventHandler.handle_event(event_data_1)
    EventHandler.handle_event(event_data_2)
    response = EventHandler.handle_event(event_data_3)
    assert not response['alert']
    assert 123 not in response['alert_codes']
