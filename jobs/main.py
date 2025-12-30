from sites.mercadolivre import MercadoLivreScrapper


mercadolivre = MercadoLivreScrapper("https://www.mercadolivre.com.br/bola-basquete-tarmak-r100-tamanho-7-laranja-claro-borracha-treinamento/p/MLB26914278?pdp_filters=item_id:MLB4002879661#is_advertising=true&searchVariation=MLB26914278&backend_model=search-backend&position=1&search_layout=grid&type=pad&tracking_id=8bc77860-786f-428e-bde0-278414076c88&ad_domain=VQCATCORE_LST&ad_position=1&ad_click_id=YzQxMWMwMjYtMzQ2ZS00MmY1LTk4NGEtYTM3ZDQxMDEwOTY4")
print(mercadolivre.get_price())