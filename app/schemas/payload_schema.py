from pydantic import BaseModel

class PayloadSchema(BaseModel):
    description: str
    url: str
    target_price: float
    duration_minutes: int