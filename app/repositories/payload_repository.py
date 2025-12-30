from app.models.payload_model import Payload
from app.schemas.payload_schema import PayloadSchema
from sqlalchemy.orm import Session

class PayloadRepository:
    async def create_payload(db_session: Session, payload_data:PayloadSchema):
        from app.models.payload_model import Payload
        new_payload = Payload(description=payload_data.description, target_price=payload_data.target_price, url=payload_data.url, duration_minutes=payload_data.duration_minutes)
        db_session.add(new_payload)
        db_session.commit()
        db_session.refresh(new_payload)
        return new_payload
    
    async def get_payload(db_session: Session):
        from app.models.payload_model import Payload
        return db_session.query(Payload).all()