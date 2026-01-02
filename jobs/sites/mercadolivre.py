from services.history_services import HistoryServices 
from core.base import BaseScrapper
from models.HistoryModel import History
from playwright.async_api  import async_playwright
from dependencies.database_dependencies import get_db
from datetime import date

class MercadoLivreScrapper(BaseScrapper):   
    def __init__(self, url: str):
          super().__init__(url)

    async def get_price(self, payload_id) -> float:
        async with async_playwright() as p:
            browser = await p.chromium.launch(
                headless=True,
                args=["--disable-blink-features=AutomationControlled"]
            )

            context = await browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
                locale="pt-BR",
                viewport={"width": 1280, "height": 800}
            )

            page = await context.new_page()

            await page.goto(self.url, wait_until="networkidle", timeout=60000)

            await page.wait_for_function("""
                () => {
                    const el = document.querySelector('span.andes-money-amount__fraction');
                    return el && el.innerText.trim().length > 0;
                }
            """, timeout=60000)

            price_text = await page.locator(
                "#price > div > div.ui-pdp-price__main-container > div.ui-pdp-price__second-line > span.ui-pdp-price__part__container > span > span.andes-money-amount__fraction"
            ).first.inner_text()

            history_services = HistoryServices()
            await history_services.create_history(get_db(), history=History(
                url=self.url,
                old_price=float(
                    price_text.replace(".", "").replace(",", ".")
                ),
                new_price=float(
                    price_text.replace(".", "").replace(",", ".")
                ),
                change_date=date.today(),
                payload_id=payload_id
            ))

            await browser.close()
        return float(
            price_text.replace(".", "").replace(",", ".")
        )
        
        
    def get_title(self):
         return super().get_title()