from urllib.request import urlopen
from bs4 import BeautifulSoup

myurl = 'https://comic.naver.com/webtoon/weekday'

# 이 페이지에 request해서 데이터를 가져온 후 변수에 저장한다.
response = urlopen(myurl)

# <class 'http.client.HTTPResponse'>
print(type(response))

# BeautifulSoup()를 이용해서 데이터를 파싱한다.
soup = BeautifulSoup(response, 'html.parser')

# Beautiful Soup 객체를 적절한 들여쓰기 형태로 출력해준다.
# print(soup.prettify())

title = soup.find("title").string
print(title)


