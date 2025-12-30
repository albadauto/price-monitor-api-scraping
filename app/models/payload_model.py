from sqlalchemy import Column, Integer, String, Float
from app.core.database import Base

class Payload(Base):
    __tablename__ = "payloads"  
    
    id = Column(Integer, primary_key=True, index=True)
    data = Column(String, index=True)
    description = Column(String, index=True)
    url = Column(String, index=True )
    target_price = Column(Float, index=True)
    duration_minutes = Column(Integer, index=True)