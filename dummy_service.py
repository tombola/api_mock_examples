import requests
from dummy_api import PRODUCTS_API_URL

def get_products():
    return requests.get(PRODUCTS_API_URL)