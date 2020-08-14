import requests
from urllib.parse import urlparse
result = requests.get(urlparse("https://openapi.naver.com/v1/search/blog?query=" + "에어컨").geturl(),
            headers={"X-Naver-Client-Id":"",
                     "X-Naver-Client-Secret":""})
print(result)