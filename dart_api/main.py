import Python_crawling.dart_api.module.call_excel as cc
import Python_crawling.dart_api.module.dart_module as dm

# 현재 날짜를 기점으로 자동으로 분기 설정 하게끔 설계할예정
# number = input('only input number  ex) 1 , 2 ,3 , 4(온기) : ')
cc.save_stock_value(dm.open_dart(cc.call_cc(),
                                 '2' # number변수 대신 편의를 위해 임의로 강제설정
                                 ))
