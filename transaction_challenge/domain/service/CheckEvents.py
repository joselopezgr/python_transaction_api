from transaction_challenge.domain.service.checkBase import CheckAbstractInterface 

# 1. Check: if the amount withdrew is more than 100 throw alert 1100
class WithdrawalAmountCheck(CheckAbstractInterface):
    def check(self, event, transactions) -> int:
        # Given `amount` is string we have to convert it to integer
        amount = float(event.amount)
        
        # First check if its the right type and check for amount withdrew
        if event.type == "withdrawal" and amount > 100:
            return 1100
        return 0

# 2. Check: if 3 consecutive withdrawals throw alert 30
class WithdrawalLengthCheck(CheckAbstractInterface):
    def check(self, event, transactions) -> int:
        consecutive_withdrawals = 0
        
        # Loop through the transactions made and if withdrawal then increase counter
        for transaction in transactions:
            if transaction.type == "withdrawal":
                consecutive_withdrawals += 1
                if consecutive_withdrawals >= 3:
                    return 30
            # Otherwise, set counter to 0 to keep consecutive-ness (could this be a word?)
            else:
                consecutive_withdrawals = 0
        return 0
    
# 3. Check: if deposit incremental amounts more than 3 times throw alert 300       
class ConsecutiveDepositsCheck(CheckAbstractInterface):
    def check(self, event, transactions) -> int:
        counter = 1
        # Loop that checks if amount posted is bigger than existing one, if its then incrase counter 
        for transaction in transactions:
            if transaction.type == "deposit" and float(transaction.amount) < float(event.amount):
                counter += 1
        if counter >= 3:
            return 300
        return 0
    
# 4. Check: if total amount > 200 in 30 sec time frame throw alert 123
class DepositTimeAmountCheck(CheckAbstractInterface):
    def check(self, event, transactions) -> int:
        current_time = event.time
        total_amount = 0
        # Loop to check if time is within the 30 seconds if is then update total_amount
        for transaction in transactions:
            if transaction.type == "deposit" and 0 <= current_time - transaction.time <= 30:
                total_amount += float(transaction.amount)
        if total_amount > 200:
            return 123
          
        return 0
