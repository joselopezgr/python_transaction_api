from transaction_challenge.domain.dto.clientTransactionDto import ClientTransactionDto
from transaction_challenge.domain.dto.eventResponseDto import EventResponseDto
from transaction_challenge.domain.service.CheckEvents import WithdrawalAmountCheck, WithdrawalLengthCheck, DepositTimeAmountCheck, ConsecutiveDepositsCheck
from typing import List

class EventHandler:
    # In-memory array list storage to keep track of transations (otherwise use DB)
    depositTransactions = []
    withdrawalTransactions = []
    
    @staticmethod
    def handle_event(event_data: ClientTransactionDto) -> EventResponseDto:
        #Initialize a in-memory array of alerts
        alert_codes: List[int] = []
        
        #Here we check the type of transaction and group them together
        if event_data.type == "deposit":
            EventHandler.depositTransactions.append(event_data)
            transactions = EventHandler.depositTransactions
        else:
            EventHandler.withdrawalTransactions.append(event_data)
            transactions = EventHandler.withdrawalTransactions
            
        # Iterate through the different methods (Future Improvement: Use Strategy Pattern instead)
        checks = [
            WithdrawalAmountCheck(),
            WithdrawalLengthCheck(),
            ConsecutiveDepositsCheck(),
            DepositTimeAmountCheck()
        ]
        
        # Iterate through those methods and run each one of them feeding necessary parameters
        for check in checks:
            alert_code = check.check(event_data, transactions)
            # Only append the codes if it isnt zero
            if alert_code != 0:
                alert_codes.append(alert_code)
        # Construct the response dto, doing a check to return false if no codes found
        response_dto = EventResponseDto(alert=False if len(alert_codes) == 0 else True, alert_codes=alert_codes, user_id=event_data.user_id)
        # This model_dump method will generate a dictionary of the eventResponse object
        return response_dto.model_dump()
