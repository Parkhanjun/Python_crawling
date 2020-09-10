import openpyxl as excel
import pandas as pd


def call_cc():
    lis = []
    ex_load = excel.load_workbook('C:/Users/safa6/git/python/Python_crawling/dart_api/excel/stock.xlsx')
    sheet = ex_load['Sheet1']
    for row in sheet.rows:
        lis.append(row[0].value)
    return lis


def save_stock_value(open):
    print(open)
    file_name = open['a']
    open.pop('a')
    pandas = pd.DataFrame(open)
    pandas.to_excel(f'C:/Users/safa6/git/python/Python_crawling/dart_api/excel/{file_name}.xlsx',
               sheet_name='Sheet1',
               )



if __name__ == "__main__":
    call_cc()