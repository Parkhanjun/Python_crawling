# csv 확장자로 하여야 엑셀에 저장할 수 있음  , w+ 지속적으로 저장 가능하게 함
file = open("./hello.csv","w+")
file.write("hello" + "\n") #
file.write("BYE" + "\n")