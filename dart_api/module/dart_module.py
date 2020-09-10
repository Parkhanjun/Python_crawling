import calendar
import datetime
import requests
import json
import re
from bs4 import BeautifulSoup as bs
from html_table_parser import parser_functions as parser


def date(number):
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
        start_month = '01'
        end_month = '03'
    today = datetime.date.today()
    year = today.year
    last_day = calendar.monthrange(year, int(end_month.split('0')[1]))[1]
    begin = str(year) + start_month + '01'
    end = str(year) + end_month + str(last_day)
    return [begin, end]


def company_code(code,number):
    key = '키 입력'
    date_li = []
    for item in date(number):
        date_li.append(item)
    print(date_li)
    type = 'A'  # B , C , D 타입에 따라 결과값 다름,즉 추가코딩 하여야함
    list = []
    for arr in code:
        url = f"https://opendart.fss.or.kr/api/list.json?crtfc_key={key}&corp_code={arr}&bgn_de={date_li[0]}" \
              f"&end_de={date_li[1]}&pblntf_ty={type}&corp_cls={'Y'}&page_no=1&page_count=10"
        if json.loads(requests.get(url).text)['status'] != '000':
            url = f"https://opendart.fss.or.kr/api/list.json?crtfc_key={key}&corp_code={arr}&bgn_de={date_li[0]}" \
                  f"&end_de={date_li[1]}&pblntf_ty={type}&corp_cls={'K'}&page_no=1&page_count=10"
        result = requests.get(url).text
        print(result)
        li = json.loads(result)['list']
        for arr in li:
            if arr['rm'] == '연':
                pass
            else:
                list.append(arr['rcept_no'])
    # print(list)
    return list


def open_dart(code,number):
    ttr = {}
    for it in company_code(code,number):
        url = 'http://dart.fss.or.kr/dsaf001/main.do?rcpNo=' + it
        html = requests.get(url).text
        title = bs(requests.get(url).text,'html.parser').find('title')
        split = re.split('연결재무제표', html)[1].split(r');')[0].split(r'viewDoc(')[1].replace("'","").split(', ')
        rurl = f'http://dart.fss.or.kr/report/viewer.do?rcpNo={split[0]}&dcmNo={split[1]}&eleId={split[2]}&offset={split[3]}&length={split[4]}&dtd={split[5]}'
        result = bs(requests.get(rurl).content,'html.parser')
        body = str(result).split('연결 손익계산서')[1]
        body = bs(body,'html.parser')
        tr = body.find('table')
        table = parser.make2d(tr)
        ttr['a'] = title.text.replace('/','_').replace('\n','')
        ttr['b'] = table
    return ttr


if __name__ == "__main__":
    # open_dart(code)
    print()
