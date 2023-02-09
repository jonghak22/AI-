import re 
from bs4 import BeautifulSoup

myencoding = 'utf-8'
myparser = 'html.parser'
filename = 'css01.html'

html = open(filename, encoding=myencoding)
soup = BeautifulSoup(html, myparser)

h1 = soup.select_one("div#cartoon > h1").string
print("h1 =", h1)

li_list = soup.select("div#cartoon > ul.elements > li")
li_list

for li in li_list:
    print("li =", li.string)

print('-' * 20)

choice = lambda x : print(soup.select_one(x).string)
print(choice)

soup.select_one("#item3").string

print('\nchoice("#item3") : ', end='')
choice("#item3")

print('\nchoice("li#item4") : ', end='')
choice("li#item4")

print('\nchoice("ul > li#item3") : ', end='')
choice("ul > li#item3")

print('\nchoice("#itemlist #item2") : ', end='')
choice("#itemlist #item2")

print('\nchoice("#itemlist > #item3") : ', end='')
choice("#itemlist > #item3")

print('\nchoice("ul#itemlist > li#item2") : ', end='')
choice("ul#itemlist > li#item2")

print('\nchoice("li[id=\'item1\']") : ', end='')
choice("li[id='item1']")

print('\nchoice("li:nth-of-type(4)") : ', end='')
choice("li:nth-of-type(4)")

print('\nsoup.select("li")[1].string : ', end='')
print(soup.select("li")[1].string)

print('\nsoup.find_all("li")[3].string : ', end='')
print(soup.find_all("li")[3].string)

print('-'*20)
mytag = soup.select_one('div#cartoon > ul.elements')
mystring = mytag.select_one('li:nth-of-type(3)').string
print(mystring)

print('-'*20)

mytag = soup.select_one('ul#itemlist')
mystring = mytag.select_one('li:nth-of-type(4)').string
print(mystring)
print('-'*20)

# class 속성이 us인 1번째 요소
print(soup.select("#vegatables > li[class='us']")[0].string)
print(soup.select("#vegatables > li.us")[1].string)

# ^= :  ~으로 시작하는, $= :  ~으로 끝나는
result = soup.select('a[href$=".com"]')
for item in result :
    print(item['href'])

# *= :  daum을 포함하고 있는
result = soup.select('a[href*="daum"]')
for item in result :
    print(item['href'])

# find 메서드로 추출하기
cond = {"id":"ko", "class":"cn"}
print(soup.find("li", cond).string)

# find 메서드를 연속적으로 사용하기
print(soup.find(id="vegatables").find("li", cond).string)

print('-' * 20)

print('# 정규 표현식으로 href에서 https인 것 추출하기')
li = soup.find_all(href=re.compile(r"^https://"))

for e in li:
    print(e.attrs['href'])

print('\n# finished')


