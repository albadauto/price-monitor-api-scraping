from models.HistoryModel import History

class HistoryServices:
    async def create_history(self, db, history: History):
        from repositories.HistoryRepositories import HistoryRepositories
        history_repo = HistoryRepositories()
        return await history_repo.create_history(db, history)