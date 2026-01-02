from core.base import BaseScrapper
from services.history_services import HistoryServices
from models.HistoryModel import History
from datetime import date
from dependencies.database_dependencies import get_db
from playwright.async_api  import async_playwright
class AmazonScrapping(BaseScrapper):
    def __init__(self, url: str):
        super().__init__(url)

    async def get_price(self, payload_id: int) -> float:
       async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False, args=["--disable-blink-features=AutomationControlled"])
            context = await browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
                locale="pt-BR",
                viewport={"width": 1280, "height": 800}
            )
            
            page = await context.new_page()
            
            await page.goto(self.url)

            await page.wait_for_selector(".a-price-whole")

            whole = await page.text_content(".a-price-whole")
            fraction = await page.text_content(".a-price-fraction")
            await browser.close()
            
            price = f"{whole}{fraction}"
            history_services = HistoryServices()
            await history_services.create_history(get_db(), history=History(
                old_price=float(
                    price.replace(".", "").replace(",", ".")
                ),
                new_price=float(
                    price.replace(".", "").replace(",", ".")
                ),
                change_date=date.today(),
                payload_id=payload_id
            ))
            return float(
                price.replace(".", "").replace(",", ".")
            )

    def get_title(self) -> str:
        return super().get_title()