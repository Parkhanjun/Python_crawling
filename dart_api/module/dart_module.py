import calendar
import datetime
import requests
import json
import re
from bs4 import BeautifulSoup as bs
from html_table_parser import parser_functions as parser


def date():
    today = datetime.date.today()
    year = today.year
    first_day = calendar.monthrange(year, 1)[1]
    last_day = calendar.monthrange(year, 12)[1]
    begin = str(year) + '01' + str(first_day)
    end = str(year) + '12' + str(last_day)
    return {'a': begin, 'b': end}


def company_code(code):
    key = '키'
    begin = date().get('a')
    end = date().get('b')
    type = 'A'  # B , C , D 타입에 따라 결과값 다름,즉 추가코딩 하여야함
    list = []
    for arr in code:
        url = f"https://opendart.fss.or.kr/api/list.json?crtfc_key={key}&corp_code={arr}&bgn_de={begin}" \
              f"&end_de={end}&pblntf_ty={type}&corp_cls={'Y'}&page_no=1&page_count=10"
        if json.loads(requests.get(url).text)['status'] != '000':
            url = f"https://opendart.fss.or.kr/api/list.json?crtfc_key={key}&corp_code={arr}&bgn_de={begin}" \
                  f"&end_de={end}&pblntf_ty={type}&corp_cls={'K'}&page_no=1&page_count=10"
        result = requests.get(url).text
        li = json.loads(result)['list']
        for arr in li:
            if arr['rm'] == '연':
                pass
            else:
                list.append(arr['rcept_no'])
    # print(list)
    return list


def open_dart(code):
    ttr = []
    for it in company_code(code):
        url = 'http://dart.fss.or.kr/dsaf001/main.do?rcpNo=' + it
        html = requests.get(url).text
        split = re.split('연결재무제표', html)[1].split(r');')[0].split(r'viewDoc(')[1].replace("'","").split(', ')
        rurl = f'http://dart.fss.or.kr/report/viewer.do?rcpNo={split[0]}&dcmNo={split[1]}&eleId={split[2]}&offset={split[3]}&length={split[4]}&dtd={split[5]}'
        print(rurl)
        result = bs(requests.get(rurl).content,'html.parser')
        body = str(result).split('연결 손익계산서')[1]
        body = bs(body,'html.parser')
        tr = body.find('table')
        table = parser.make2d(tr)
        ttr.append(table)
    return ttr

# 예외의 상황 발생시 대처할 예외처리들을 코딩하기
'''
하다가 방법을 모르겠어서 결국 버려진 셀레니움코드...
# driver = webdriver.Chrome('chromedriver.exe')
# driver.get(http)
# west = driver.find_element_by_css_selector('.x-tree-root-node').find_elements_by_tag_name('li')
# for tag in west:
#     if '2. 연결재무제표' == tag.text:
tag.click()
클릭 이후 url이 안바뀌는 구조여서 클릭이전 url만 반환함 
a태그 href 조회를 해봐도 href=# 이어서 조회가 불가함
'''

if __name__ == "__main__":
    # open_dart(code)
    print()
