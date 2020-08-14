import requests
from bs4 import BeautifulSoup as bs

def get_bs4_obj(url):
    return bs(requests.get(url).content, "html.parser")