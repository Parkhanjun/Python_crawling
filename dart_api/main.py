import Python_crawling.dart_api.module.call_excel as cc
import Python_crawling.dart_api.module.dart_module as dm

number = input('분기를 숫자로만 입력하세요 ex) 1 , 2 ,3 , 4(온기) : ')
cc.save_stock_value(dm.open_dart(cc.call_cc(),number))

#
# number = input('입력 : ')
# if number == '1':
#     print('good')