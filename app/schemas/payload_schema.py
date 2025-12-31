from pydantic import BaseModel
from datetime import date
class PayloadSchema(BaseModel):
    description: str
    url: str
    target_price: float
    status: str = "pending"
    queue: int
    initial_date: date
    end_date: date