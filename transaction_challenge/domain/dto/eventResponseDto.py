from pydantic import BaseModel
from typing import List

class EventResponseDto(BaseModel):
    alert: bool
    alert_codes: List[int]
    user_id: int