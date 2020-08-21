import calendar
import datetime
import requests
import pandas as pd
import json


def date():
    today = datetime.date.today()
    year = today.year
    first_day = calendar.monthrange(year, 1)[1]
    last_day = calendar.monthrange(year, 12)[1]
    begin = str(year) + '01' + str(first_day)
    end = str(year) + '12' + str(last_day)
    return {'a':begin , 'b':end}


def company_code(code):
    key = '키'
    begin = date().get('a')
    end = date().get('b')
    type = 'A'   # B , C , D 타입에 따라 결과값 다름,즉 추가코딩 하여야함
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
    for item in company_code(code):
        http = 'http://dart.fss.or.kr/dsaf001/main.do?rcpNo='+item
        print(http)
    # 열린 분기실적 페이지에서 키워드 뽑아내야함



if __name__ == "__main__":
    # open_dart('005930')
    print()