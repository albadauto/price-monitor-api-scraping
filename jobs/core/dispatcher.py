async def scrape_in_mercadolivre(url: str) -> float:
    from sites.mercadolivre import MercadoLivreScrapper
    scrapper = MercadoLivreScrapper(url)
    await scrapper.get_price()
    
    
async def scrape_in_amazon(url: str) -> float:
    from sites.amazon import AmazonScrapping
    scrapper = AmazonScrapping(url)
    await scrapper.get_price()