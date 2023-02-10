import urllib.request
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import sys
now = datetime.now()

hdr = { 'User-Agent' : 'Mozilla/5.0' }
url = 'https://www.melon.com/chart/index.htm'

req = urllib.request.Request(url, headers=hdr)
html = urllib.request.urlopen(req).read()
soup = BeautifulSoup(html, 'html.parser')

lst = soup.select('.lst50,.lst100')
rank = 1


# 실시간 멜론차트를 txt 파일에 저장
# sys.stdout = open('./Desktop/auto/Melonchart.txt','a')
# print()
# print('멜론 실시간 TOP100차트 : '+str(now)+' 기준 ')
# print()
# for i in lst:
#     sys.stdout = open('./Desktop/auto/Melonchart.txt','a')
#     print(str(rank)+'위', end=' ')
#     print(i.select_one('.ellipsis.rank01').a.text, end=' ')
#     print(i.select_one('.ellipsis.rank02').a.text, end=' ')
#     print(i.select_one('.ellipsis.rank03').a.text)
#     print()
#     sys.stdout = open('./Desktop/auto/Melonchart.txt','a')
#     rank+=1


#실시간 멜론차트를 cvs (엑셀파일) 형식으로 저장
melonList=[]
for j in lst:
    temp = []
    temp.append(str(rank))
    temp.append(j.select_one('.ellipsis.rank01').a.text)
    temp.append(j.select_one('.ellipsis.rank02').a.text)
    temp.append(j.select_one('.ellipsis.rank03').a.text)
    melonList.append(temp)
    rank+=1

with open('Newmelon100.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['순위','아티스트','곡명','앨범','출력시간 :  '+str(now)])
    writer.writerows(melonList)
