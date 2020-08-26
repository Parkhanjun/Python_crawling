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
    panda = pd.DataFrame(open)
    excel_panda = pd.ExcelWriter('C:/Users/safa6/git/python/Python_crawling/dart_api/excel/test.xlsx')
    panda.to_excel(excel_panda, sheet_name='Sheet1')
    excel_panda.save()
    excel_panda.close()

    # write = excel.Workbook().active
    # write.append(open)
    # Workbook().save('C:/Users/safa6/git/python/Python_crawling/dart_api/excel/test.xlsx')
    # Workbook().close()
    return print('끝')

if __name__ == "__main__":
    call_cc()