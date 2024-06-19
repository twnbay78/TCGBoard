import requests
from typing import Any
from dataclasses import dataclass

class TcgPlayerConnector:
    hostname = "tcgplayer.com"
    def __init__(self) -> None:
        print("Initializing TCGPlayerConnector with hostname: " + self.hostname)

class MarketplaceSearchConnector(TcgPlayerConnector):
    subdomain = "mp-search-api"
    def __init__(self) -> None:
        super().__init__()
        self.fqdn = "https://" + MarketplaceSearchConnector.subdomain + "." + self.hostname
    
    def call(self, method: str, path: str) -> Any:
        return requests.request(method, self.fqdn + path)
    
    def get_product_details_by_id(self, product_id: int) -> Any:
        return self.call("GET", "/v1/product/" + str(product_id)) + "/details?mpfev=2487"
    
    def get_product_details_by_url_name(self, url_name: str) -> Any:
        return self.call("GET", "/v1/product/" + str(TcgPlayerData.product_url_name_id_map[url_name]) + "/details?mpfev=2487")

    def get_market_price_by_url_name(self, url_name: int) -> Any:
        resp_data = self.get_product_details_by_url_name(url_name)
        return resp_data.json()['marketPrice']
    
    def get_lowest_price_with_shipping_by_url_name(self, url_name: int) -> Any:
        resp_data = self.get_product_details_by_url_name(url_name)
        return resp_data.json()['lowestPriceWithShipping']


    
@dataclass
class TcgPlayerData:
    product_url_name_id_map = {
        "Modern Horizons 3 Collector Booster Display": 541179
    }