from domain.service.checkBase import CheckAbstractInterface 
from domain.dto.clientTransactionDto import ClientTransactionDto 
from typing import List      

# 1. Check if event.type == "withdrawal" && .amount is more than 100 then throw alert 1100
class WithdrawalAmountCheck(CheckAbstractInterface):
    def check(self, event, transactions) -> int:
        # Given `amount` is string we have to convert it to integer
            amount = float(event.amount)
            
            if(event.type == "withdrawal" and amount > 100):
                return 1100
            return 0

# 2. Check if event.type == "withdrawal" && number of transactions > 3 throw alert 30
class WithdrawalLengthCheck(CheckAbstractInterface):
    def check(self, event, transactions) -> int:
        counter = 0
        
        for transaction in transactions:
            if(transaction.type == "withdrawal"):
                counter += 1
        if counter >= 3:
            return 30
        return 0
    
# 3. Check if event.type == "deposit" && incremental consecutive deposits (ignore in between) throw alert 300        
class ConsecutiveDepositsCheck(CheckAbstractInterface):
    def check(self, event, transactions) -> int:
        counter = 1
        
        for transaction in transactions:
            if transaction.type == "deposit" and transaction.amount < event.amount:
                counter += 1
        if counter >= 3:
            return 300
        return 0
    
# 4. Check if event.type == "deposit" && event.time
class DepositTimeAmountCheck(CheckAbstractInterface):
    def check(self, event, transactions) -> int:
        transaction_window: List[ClientTransactionDto] = []
        
        if(event.type == "deposit"):
            transaction_window.append(event)
        
        return 0
