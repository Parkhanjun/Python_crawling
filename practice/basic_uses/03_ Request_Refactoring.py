import time
from multiprocessing import Pool
# 불필요한 코드 줄이기
import requests
from bs4 import BeautifulSoup as bs


def get_bs4_obj(url):
    return bs(requests.get(url).content, "html.parser")


def get_stock_value(keyword):
    url = "https://finance.naver.com/item/main.nhn?code=" + keyword
    tbody = get_bs4_obj(url).find("table", {"class": "no_info"}).findAll("tr") #[0],[1]
    now = get_bs4_obj(url).find("p", {"class": "no_today"}).find("span", {"class": "blind"}) #현재가

    close = tbody[0].find("td", {"class": "first"}).find("span", {"class": "blind"})  # 전일종가
    high = tbody[0].findAll("td")[1].find("span", {"class": "blind"})
    start = tbody[1].find("td",{"class":"first"}).find("span", {"class": "blind"})
    low = tbody[1].findAll("td")[1].find("span", {"class": "blind"})

    #all test
    print("현:"+now.text, "전종:"+close.text, "고"+high.text, "시작"+start.text , "저"+low.text)

    return {
        "현재가 : " +now.text ,
        "전일종가 : " +close.text,
        "고가 : " +high.text,
        "시가 : " +start.text,
        "저가 : " +low.text
            }

get_stock_value("005930") # 임시 테스트용

if __name__ == '__main__':
    lis = [
        '005930',
        '000660',
    ]
    pool = Pool(processes=4)
    start_time = time.time()
    # print(pool.map(get_stock_value, lis))
    print("실행 시간 : %s초" % (time.time() - start_time))
