from repositories.PayloadRepositories import PayloadRepositories
from sqlalchemy.orm import Session
class PendingServices:
    async def fetch_pending_services(session: Session):
        pending_payload = await PayloadRepositories.load_pending_payloads(session)
        return pending_payload  