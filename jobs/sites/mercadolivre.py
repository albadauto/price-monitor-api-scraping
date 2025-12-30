import requests
from bs4 import BeautifulSoup
from core.base import BaseScrapper
import re
from playwright.sync_api import sync_playwright


class MercadoLivreScrapper(BaseScrapper):   
    def __init__(self, url: str):
          super().__init__(url)

    def get_price(self) -> float:
        with sync_playwright() as p:
            browser = p.chromium.launch(
                headless=True,
                args=["--disable-blink-features=AutomationControlled"]
            )

            context = browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
                locale="pt-BR",
                viewport={"width": 1280, "height": 800}
            )

            page = context.new_page()

            page.goto(self.url, wait_until="networkidle", timeout=60000)

            page.wait_for_function("""
                () => {
                    const el = document.querySelector('span.andes-money-amount__fraction');
                    return el && el.innerText.trim().length > 0;
                }
            """, timeout=60000)

            price_text = page.locator(
                "#price > div > div.ui-pdp-price__main-container > div.ui-pdp-price__second-line > span.ui-pdp-price__part__container > span > span.andes-money-amount__fraction"
            ).first.inner_text()

            browser.close()

        return float(
            price_text.replace(".", "").replace(",", ".")
        )
    def get_title(self):
         return super().get_title()