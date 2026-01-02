from sqlalchemy import Column, Integer, String, Float, Date
from database.database import Base

class History(Base):
    __tablename__ = "history"
    id = Column(Integer, primary_key=True, index=True)
    payload_id = Column(Integer, index=True)
    old_price = Column(Float, index=True)
    new_price = Column(Float, index=True)
    change_date = Column(Date, index=True)