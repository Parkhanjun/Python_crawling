import openpyxl as excel
import pandas as pd
import numpy as np


def call_cc():
    lis = []
    ex_load = excel.load_workbook('C:/Users/safa6/git/python/Python_crawling/dart_api/excel/stock.xlsx')
    sheet = ex_load['Sheet1']
    for row in sheet.rows:
        lis.append(row[0].value)

    return lis


def save_stock_value(open):
    list = []
    for item in open:
        list.append(item)
    pan1 = pd.DataFrame(list[0])
    pan2 = pd.DataFrame(list[1])
    pc = pd.concat([pan1,pan2], axis=1)
    panda = pd.DataFrame(pc)
    panda.to_excel('C:/Users/safa6/git/python/Python_crawling/dart_api/excel/test.xlsx',
                   sheet_name='Sheet1',
                   )


if __name__ == "__main__":
    call_cc()