import calendar
import datetime
import requests
import json
import re


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
        url = "https://opendart.fss.or.kr/api/list.json?crtfc_key=" + key + \
              "&corp_code=" + arr + "&bgn_de=" + begin + "&end_de=" + end + "&pblntf_ty=" + type + "&corp_cls=Y&page_no=1&page_count=10"
        if json.loads(requests.get(url).text)['status'] != '000':
            url = "https://opendart.fss.or.kr/api/list.json?crtfc_key=" + key + \
                  "&corp_code=" + arr + "&bgn_de=" + begin + "&end_de=" + end + "&pblntf_ty=" + type + "&corp_cls=K&page_no=1&page_count=10"
        result = requests.get(url).text
        li = json.loads(result)['list']
        for arr in li:
            list.append(arr['rcept_no'])
    return list


def open_dart(code):
    http = ''
    for item in company_code(code):
       http = 'http://dart.fss.or.kr/dsaf001/main.do?rcpNo=' + item
    html = requests.get(http).text
    split = re.split(r'연결재무제표',html)[1].split(r';')[0].split(r'viewDoc(')[1].split(r',')
    print(split)

    # split값 url 파라미터에 파싱하고 얻은 html에서 재무제표 테이블값을 리턴 시키기
    # 예외의 상황 발생시 대처할 예외처리들을 코딩하기
    # 끝

    return split



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
