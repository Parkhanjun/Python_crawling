import calendar
import datetime
import requests
import json
import re
from bs4 import BeautifulSoup as bs
from html_table_parser import parser_functions as parser
from IPython.display import display


def date(number):
    today = datetime.date.today()
    year = today.year
    if number == '1':
        start_month = '04'
        end_month = '05'
    if number == '2':
        start_month = '07'
        end_month = '08'
    if number == '3':
        start_month = '10'
        end_month = '11'
    if number == '4':
        year = int(year) + 1
        start_month = '01'
        end_month = '03'
    if end_month.find('0') == -1:
        last_day = calendar.monthrange(year, int(end_month))[1]
    else:
        last_day = calendar.monthrange(year, int(end_month.split('0')[1]))[1]
    begin = str(year) + start_month + '01'
    end = str(year) + end_month + str(last_day)
    return [begin, end]


def company_code(code, number):
    date_li = []
    for item in date(number):
        date_li.append(item)
    print(date_li)  # 들어가는 날짜
    key = ''
    type = 'A'  # B , C , D 타입에 따라 추가코딩 하여야함
    list = []
    for arr in code:
        url = f"https://opendart.fss.or.kr/api/list.json?crtfc_key={key}&corp_code={arr}&bgn_de={date_li[0]}" \
              f"&end_de={date_li[1]}&pblntf_ty={type}&corp_cls={'Y'}&page_no=1&page_count=10"
        if json.loads(requests.get(url).text)['status'] != '000':
            url = f"https://opendart.fss.or.kr/api/list.json?crtfc_key={key}&corp_code={arr}&bgn_de={date_li[0]}" \
                  f"&end_de={date_li[1]}&pblntf_ty={type}&corp_cls={'K'}&page_no=1&page_count=10"
        result = requests.get(url).text
        # print('status 확인',result)
        li = json.loads(result)
        if li['status'] == '013':
            print("message : 조회된 데이타가 없습니다.")
            continue
        lis = list.append(li['list'][0]['rcept_no'])
    return list


def open_dart(code, number):
    ttr = {}
    for index, it in enumerate(company_code(code, number)):
        url = 'http://dart.fss.or.kr/dsaf001/main.do?rcpNo=' + it
        html = requests.get(url).text
        title = bs(requests.get(url).text, 'html.parser').find('title')
        split = re.split('연결재무제표', html)[1].split(r');')[0].split(r'viewDoc(')[1].replace("'", "").split(', ')
        rurl = f'http://dart.fss.or.kr/report/viewer.do?rcpNo={split[0]}&dcmNo={split[1]}&eleId={split[2]}&offset={split[3]}&length={split[4]}&dtd={split[5]}'
        print(rurl)
        result = bs(requests.get(rurl).text, 'html.parser')
        re_title = result.select('html > body > table')[2].select_one('tbody > tr > td').findChild().text
        rt = str(re_title).replace(' ', '')
        print('re_title ==== ', rt)
        if rt == '연결손익계산서' or rt == '연결포괄손익계산서':
            tbody = str(result).split(re_title)[1]
        body = bs(tbody, 'html.parser')
        tr = body.find('table')
        table = parser.make2d(tr)
        ttr['a' + str(index)] = title.text.split('/')[0].replace('\n', '') + '_' + number + '분기'
        ttr['b' + str(index)] = data_set(table)
    return ttr


def data_set(make2d_tr_table):
    want = ['수익(매출액)', '영업이익', '영업이익(손실)', '당기순이익(손실)', '영업수익']
    want_table = []
    for idx, item in enumerate(make2d_tr_table):
        # if bool(item[0] in want):
        re.sub('[a-zA-Z0-9()_.+-]', '', item[0]).replace(' ', '')
        want_table.append(make2d_tr_table[idx])
    return want_table

# if __name__ == "__main__":
#     # open_dart(code)
#     print('d')
