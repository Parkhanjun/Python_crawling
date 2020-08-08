# return 은 function 내부의 은 연산을 다른곳에서도 사용하기 위함
# 함수 바깥에서도 사용하려면 return을 활용해라
def add(val1,val2):
    print("function_inside_print:", val1+val2)
    p="return_print :"
    return p, val1+val2

result = add(3,4)
print(result)
