from sqlalchemy.orm import Session
from models.PayloadModel import Payload
class PayloadRepositories:
    async def load_pending_payloads(db_session: Session):
        return db_session.query(Payload).filter(Payload.status == "pending").order_by(Payload.queue.asc()).first()