from sqlalchemy import Column, Integer, String, Float, Date
from datetime import date, timedelta
from database.database import Base

class Payload(Base):
    __tablename__ = "payloads"  
    id = Column(Integer, primary_key=True, index=True)
    data = Column(String, index=True)
    description = Column(String, index=True)
    url = Column(String, index=True )
    target_price = Column(Float, index=True)
    status = Column(String, index=True, default="pending")
    queue = Column(Integer, index=True)
    initial_date = Column(Date, index=True, default=date.today())
    end_date = Column(Date, index=True, default=date.today() + timedelta(days=7))