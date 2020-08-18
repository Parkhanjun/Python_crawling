import calendar
import datetime
import requests
import pandas as pd
import json
import webbrowser


def company_code(code):
    key = '발급받은 키'
    begin = date().get('a')
    end = date().get('b')
    type = 'A'   # B , C , D 타입에 따라 결과값 다름,즉 추가코딩 하여야함
    url = "https://opendart.fss.or.kr/api/list.json?crtfc_key="+key+ \
          "&corp_code=" + code + "&bgn_de=" + begin + "&end_de=" + end + "&pblntf_ty=" + type + "&corp_cls=Y&page_no=1&page_count=10"
    result = requests.get(url).text
    li = json.loads(result)['list']
    list = []
    for arr in li:
        list.append(arr['rcept_no'])
    return list


def open_dart(code):
    # for item in company_code(code):
    # http = 'http://dart.fss.or.kr/dsaf001/main.do?rcpNo='+item
    # webbrowser.open(http)
    print(code)


def date():
    today = datetime.date.today()
    year = today.year
    first_day = calendar.monthrange(year, 1)[1]
    last_day = calendar.monthrange(year, 12)[1]
    begin = str(year) + '01' + str(first_day)
    end = str(year) + '12' + str(last_day)
    dic = {'a':begin , 'b':end}
    return dic


if __name__ == "__main__":
    # open_dart('005930')
    print()