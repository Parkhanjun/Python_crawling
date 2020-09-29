import openpyxl as excel
import pandas as pd
from IPython.display import display
import os

def call_cc():
    lis = []
    ex_load = excel.load_workbook('C:/Users/safa6/git/python/Python_crawling/dart_api/excel/stock.xlsx')
    sheet = ex_load['Sheet1']
    for row in sheet.rows:
        lis.append(row[0].value)
    return lis


def save_stock_value(open):
    if not open:
        print('데이타가 없으므로 종료합니다')
        exit()
    for item in open:
        if item.find('a') != -1:
            folder_name = open[item].split('_')[0]
            # section = open[item].split('_')[1]
            file_name = open[item]
        if item.find('b') != -1:
            pandas = pd.DataFrame(open[item])
            # display(pandas)
            path = f'C:/Users/safa6/git/python/Python_crawling/dart_api/excel/{folder_name}'
            check_folder = os.path.isdir(path)
            if not check_folder:
                os.makedirs(path)
            pandas.to_excel(f'{path}/{file_name}.xlsx',
                            sheet_name='Sheet1',
                            )

    def option():
        print('아직 미구현')



if __name__ == "__main__":
    call_cc()