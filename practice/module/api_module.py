import requests


def get1000Result(key):
    lis = []
    for num in range(0, 10):
        lis = lis + call(key, num * 100+1)['items']
        print(lis)
    return lis


def call(key, value):
    url = "https://openapi.naver.com/v1/search/blog?query="+key+"&display=100"+"&start="+str(value)
    result = requests.get(url,
            headers={"X-Naver-Client-Id":"",
                     "X-Naver-Client-Secret":""})
    return result.json()

