from core.base import BaseScrapper
from playwright.async_api  import async_playwright
class AmazonScrapping(BaseScrapper):
    def __init__(self, url: str):
        super().__init__(url)

    async def get_price(self) -> float:
       async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True, args=["--disable-blink-features=AutomationControlled"])
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
            price_text = await page.locator("#corePriceDisplay_desktop_feature_div > div.a-section.a-spacing-none.aok-align-center.aok-relative > span.a-price.aok-align-center.reinventPricePriceToPayMargin.priceToPay > span:nth-child(2) > span.a-price-whole").first.inner_text()
            await browser.close()
            
            return float(
                price_text.replace(".", "").replace(",", ".")
            )
            
            

    def get_title(self) -> str:
        return super().get_title()