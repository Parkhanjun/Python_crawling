import requests
from urllib.parse import urlparse
result = requests.get(urlparse("https://openapi.naver.com/v1/search/blog?query=" + "에어컨").geturl(),
            headers={"X-Naver-Client-Id":"HwQRn2emMFQhUh3R2XvA",
                     "X-Naver-Client-Secret":"ZDBVXuB3Ui"})
print(result)