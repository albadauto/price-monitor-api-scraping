from app.models.payload_model import Payload
from app.schemas.payload_schema import PayloadSchema
from sqlalchemy.orm import Session
from sqlalchemy import func

class PayloadRepository:
    async def create_payload(db_session: Session, payload_data):
        from app.models.payload_model import Payload

        last_queue = await PayloadRepository.get_last_queue_number(db_session)

        new_payload = Payload(
            description=payload_data.description,
            url=payload_data.url,
            target_price=payload_data.target_price,
            status=payload_data.status,
            queue=last_queue + 1,
            initial_date=payload_data.initial_date,
            end_date=payload_data.end_date
        )

        db_session.add(new_payload)
        db_session.commit()
        db_session.refresh(new_payload)

        return new_payload
    
    async def get_payload(db_session: Session):
        from app.models.payload_model import Payload
        return db_session.query(Payload).all()
    
    async def get_last_queue_number(db_session: Session):
        from app.models.payload_model import Payload

        last_queue = db_session.query(func.max(Payload.queue)).scalar()
        return last_queue or 0