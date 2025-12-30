from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.payload_schema import PayloadSchema
from app.dependencies.db_dependencies import get_db
route = APIRouter(tags=["Payloads"])

@route.post("/payloads")
async def create_payload(payload_data: PayloadSchema, db: Session = Depends(get_db)):
    from app.services.payload_service import PayloadService
    return await PayloadService.create_payload(db, payload_data)


@route.get("/payloads")
async def get_payloads(db: Session = Depends(get_db)):
    from app.services.payload_service import PayloadService
    return await PayloadService.get_payloads(db)