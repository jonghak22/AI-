import os

from urllib.request import urlopen
from bs4 import BeautifulSoup
from pandas import DataFrame 

myparser = 'html.parser'
myurl = 'https://comic.naver.com/webtoon/weekday.nhn'
response = urlopen(myurl)
soup = BeautifulSoup(response, myparser)
# print(result) # 결과물을 cartoon.html 파일에 복사
# print(type(result))

weekday_dict = {'mon':'월요일', 'tue':'화요일', 'wed':'수요일',
                'thu':'목요일', 'fri':'금요일', 'sat':'토요일', 
                'sun':'일요일'}

myfolder = 'c:\\imsi\\'
try :
    if not os.path.exists(myfolder): # 임시 폴더 생성
        os.mkdir(myfolder)

    for mydir in weekday_dict.values() :
        mypath = myfolder + mydir
        if os.path.exists(mypath) :
            pass
        else : # '월요일'부터 '일요일'까지 폴더 생성
            os.mkdir(mypath)
except FileExistsError as err :
    pass # 오류를 무시하고 넘깁니다.

def saveFile(mysrc, myweekday, mytitle):
    image_file = urlopen(mysrc)
    filename = myfolder + myweekday + '\\' + mytitle + '.jpg'
                   
    # print(filename)
    myfile = open(filename , mode='wb')
    myfile.write(image_file.read()) # 이미지로 저장됨

mylist = []  # 데이터를 저장할 리스트

mytarget = soup.find_all('div', attrs={'class':'thumb'})
print('만화 총 개수 : %d' % (len(mytarget)))
for abcd in mytarget :
    myhref = abcd.find('a').attrs['href']
    myhref = myhref.replace('/webtoon/list.nhn?', '')
    result = myhref.split('&')
    mytitleid = result[0].split('=')[1]
    myweekday = result[1].split('=')[1]
    myweekday = weekday_dict[myweekday]
    # print(mytitleid + '/' + myweekday)

    imgtag = abcd.find('img')
    #print(imgtag)
    mysrc = imgtag.attrs['src']
    mytitle = imgtag.attrs['title'].strip()
    mytitle = mytitle.replace('?', '').replace(':', '')

    # print(mytitle + '/' + mysrc)

    mytuple = tuple([mytitleid, myweekday, mytitle, mysrc])
    mylist.append(mytuple)

    # 이미지 저장 함수
    saveFile(mysrc, myweekday, mytitle)

print(mylist)

myframe = DataFrame(mylist, columns = ['타이틀 번호', '요일', '제목', '링크'])
filename = 'cartoon.csv'
myframe.to_csv(filename, encoding = 'cp949', index=False)
print(filename + '파일로 저장됨')
print('\n# finished')
