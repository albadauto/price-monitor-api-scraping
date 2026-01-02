from abc import ABC, abstractmethod
import requests
class BaseScrapper(ABC):
    @abstractmethod
    def __init__(self, url: str):
        self.url = url
        
    @abstractmethod
    def get_price(self, payload_id: int) -> float:
        pass
    
    @abstractmethod
    def get_title(self) -> str:
        pass
    
    
    def _fetch_page_content(self) -> str:
        headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept-Language": "pt-BR,pt;q=0.9"
        }

        response = requests.get(self.url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
