# import 를 통해 내,외부 라이브러리 사용
"""
import urllib.request
import bs4
url = "https://www.naver.com/"
html = urllib.request.urlopen(url)
bs4.BeautifulSoup(html)
bsObj = bs4.BeautifulSoup(html)
"""

# 코드 줄이기
from urllib.request import urlopen as open
from bs4 import BeautifulSoup as bs
url = "https://www.naver.com/"
bsObj = bs(open(url))


# function 활용
def find(para, para2):
    return bsObj.find(para, para2)


'''
# 1. 전체 크롤링
# print(html.read()) 전체 읽기
# print(bsObj) bs4활용 전체 읽기

# 2. 일부 크롤링 ( 탑 메뉴단 )
# top_Obj = bsObj.find("div", {"class": "service_area"})
# print(top_Obj)

# 3. 탑메뉴단 내의 "시작페이지" 텍스트뽑기
# a_tag = find("a", {"id": "NM_set_home_btn"})
# print(a_tag.text)

# 4. 메뉴 텍스트 반복 뽑기
# menu_text = find("ul", {"class": "list_nav type_fix"})
menu_text = find("div", {"class": "group_nav"}).findAll("li")
for item in menu_text:
    a_tag = item.find("a")
    print(a_tag.text)
'''

menu_text = find("div", {"class": "group_nav"}).findAll("li")

# for문 list화 , list를 for화
for_list = [item.find("a").text for item in menu_text]
for idx, titles in enumerate(for_list):
    print("메뉴 "+idx.__str__()+"\n :",titles)