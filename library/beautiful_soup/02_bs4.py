from urllib.request import urlopen as open
from bs4 import BeautifulSoup as bs
soup = bs(open('https://www.naver.com/'))


def find(Obj1, Obj2):
    return soup.find(Obj1, Obj2)


find("div", {"class":"nanan"})