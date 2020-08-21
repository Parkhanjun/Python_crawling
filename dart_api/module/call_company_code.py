# 엑셀에서 회사코드 불러오는 로직 짜야함
import openpyxl as excel


def call_cc():
    lis = []
    ex_load = excel.load_workbook('C:/Users/safa6/git/python/Python_crawling/dart_api/excel/stock.xlsx')
    sheet = ex_load['Sheet1']
    for row in sheet.rows:
        lis.append(row[0].value)

    return lis


if __name__ == "__main__":
    call_cc()