from app.repositories.payload_repository import PayloadRepository    
class PayloadService:
    
    @staticmethod
    async def create_payload(db_session, payload_data: PayloadRepository):
        new_payload = await PayloadRepository.create_payload(db_session, payload_data)
        return new_payload
    
    @staticmethod
    async def get_payloads(db_session):
        payload = await PayloadRepository.get_payload(db_session)
        return payload