import time
from multiprocessing import Pool, Manager
# 불필요한 코드 줄이기
import requests
from bs4 import BeautifulSoup as bs


def get_bs4_obj(url):
    return bs(requests.get(url).content,"html.parser")


def get_stock_value(keyword):
    url = "https://finance.naver.com/item/main.nhn?code="+keyword
    result = get_bs4_obj(url).find("p", {"class": "no_today"}).find("span", {"class": "blind"})
    return result.text


if __name__ == '__main__':
    lis = [
        '000660',
        '000660',
        '000660',
    ]
    pool = Pool(processes=4)
    start_time = time.time()
    print(pool.map(get_stock_value,lis))
    print("실행 시간 : %s초" % (time.time() - start_time))
