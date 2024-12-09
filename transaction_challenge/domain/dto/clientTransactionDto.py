from pydantic import BaseModel
from enum import Enum

# This enum class is to only allow deposit or withdrawal as transaction types
class TransactionType(str, Enum):
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"

class ClientTransactionDto(BaseModel):
    type: TransactionType
    amount: str
    user_id: int
    time: int
