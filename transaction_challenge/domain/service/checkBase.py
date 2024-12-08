from abc import ABC, abstractmethod
from domain.dto.clientTransactionDto import ClientTransactionDto
from domain.dto.eventResponseDto import EventResponseDto
from typing import List, Optional

class CheckAbstractInterface(ABC):
    @abstractmethod
    def check(self, event: Optional[ClientTransactionDto] = None, transactions: Optional[List[ClientTransactionDto]] = None) -> int:
        pass