from sqlalchemy.orm import Session
from models.HistoryModel import History
class HistoryRepositories:
    async def create_history(self, db: Session, history: History):
        db.add(history)
        db.commit()
        db.refresh(history)
        return history