from transaction_challenge.domain.dto.clientTransactionDto import ClientTransactionDto
from transaction_challenge.domain.dto.eventResponseDto import EventResponseDto
from transaction_challenge.domain.service.CheckEvents import *

class EventHandler:
    # In-memory array list storage to keep track of transations (otherwise use DB)
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
                
        response_dto = EventResponseDto(alert=False if len(alert_codes) == 0 else True, alert_codes=alert_codes, user_id=event_data.user_id)
        return response_dto.model_dump()