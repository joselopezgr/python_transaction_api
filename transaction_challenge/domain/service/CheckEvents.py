from transaction_challenge.domain.service.checkBase import CheckAbstractInterface 
from transaction_challenge.domain.dto.clientTransactionDto import ClientTransactionDto 
from typing import List      

# 1. Check if the amount withdrew is more than 100, throw 1100
class WithdrawalAmountCheck(CheckAbstractInterface):
    def check(self, event, transactions) -> int:
            # Given `amount` is string we have to convert it to integer
            amount = float(event.amount)
            
            if(event.type == "withdrawal" and amount > 100):
                return 1100
            return 0

# 2. Check if 3 consecutive withdrawals
class WithdrawalLengthCheck(CheckAbstractInterface):
    def check(self, event, transactions) -> int:
        consecutive_withdrawals = 0
        
        for transaction in transactions:
            if transaction.type == "withdrawal":
                consecutive_withdrawals += 1
                if consecutive_withdrawals >= 3:
                    return 30
            else:
                consecutive_withdrawals = 0
        return 0
    
# 3. Check if event.type == "deposit" && incremental consecutive deposits (ignore in between) throw alert 300        
class ConsecutiveDepositsCheck(CheckAbstractInterface):
    def check(self, event, transactions) -> int:
        counter = 1
        
        for transaction in transactions:
            if transaction.type == "deposit" and float(transaction.amount) < float(event.amount):
                counter += 1
        if counter >= 3:
            return 300
        return 0
    
# 4. Check if event.type == "deposit" && event.time
class DepositTimeAmountCheck(CheckAbstractInterface):
    def check(self, event, transactions) -> int:
        if event.type != "deposit":
            return 0
        
        current_time = event.time
        total_amount = 0
        
        for transaction in transactions:
            if(
                transaction.type == "deposit" and
                0 <= current_time - transaction.time <= 30
            ):
                total_amount += float(transaction.amount)
        
        if total_amount > 200:
            return 123
        
        return 0
