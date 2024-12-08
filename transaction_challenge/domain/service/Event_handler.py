from domain.dto.clientTransactionDto import ClientTransactionDto
from domain.dto.eventResponseDto import EventResponseDto
from domain.service.CheckEvents import *

class EventHandler:
    depositTransactions = []
    withdrawalTransactions = []    
    
    @staticmethod
    def handle_event(event_data: ClientTransactionDto) -> EventResponseDto:
        alert_codes: List[int] = []
        
        if (event_data.type == "deposit"):
            EventHandler.depositTransactions.append(event_data)
            transactions = EventHandler.depositTransactions
        else:
            EventHandler.withdrawalTransactions.append(event_data)
            transactions = EventHandler.withdrawalTransactions
            
        checks = [
            WithdrawalAmountCheck(),
            WithdrawalLengthCheck(),
            ConsecutiveDepositsCheck(),
            DepositTimeAmountCheck()
        ]
        
        for check in checks:
            alert_code = check.check(event_data, transactions)
            if alert_code != 0:
                alert_codes.append(alert_code)
                
        print("The Deposits: ", EventHandler.depositTransactions)
        response_dto = EventResponseDto(alert=True, alert_codes=alert_codes, user_id=event_data.user_id)
        return response_dto.model_dump()