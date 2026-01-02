async def scrape_in_mercadolivre(url: str, payload_id: int) -> float:
    from sites.mercadolivre import MercadoLivreScrapper
    scrapper = MercadoLivreScrapper(url)
    await scrapper.get_price(payload_id=payload_id)
    
    
async def scrape_in_amazon(url: str, payload_id: int) -> float:
    from sites.amazon import AmazonScrapping
    scrapper = AmazonScrapping(url)
    await scrapper.get_price(payload_id=payload_id)