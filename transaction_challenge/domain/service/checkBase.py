from abc import ABC, abstractmethod
from transaction_challenge.domain.dto.clientTransactionDto import ClientTransactionDto
from transaction_challenge.domain.dto.eventResponseDto import EventResponseDto
from typing import List, Optional

class CheckAbstractInterface(ABC):
    @abstractmethod
    def check(self, event: Optional[ClientTransactionDto] = None, transactions: Optional[List[ClientTransactionDto]] = None) -> int:
        pass