from services.pending_services import PendingServices
import asyncio
from database.database import Sessionlocal
from core.dispatcher import scrape_in_mercadolivre, scrape_in_amazon
async def main():
    db = Sessionlocal()
    try:
        pending = await PendingServices.fetch_pending_services(db)
        if "mercadolivre.com" in pending.url:
            await scrape_in_mercadolivre(pending.url)
        elif "amazon.com" in pending.url:
            await scrape_in_amazon(pending.url)
    finally:
        db.close()


if __name__ == "__main__":
    asyncio.run(main())