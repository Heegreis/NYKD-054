import requests
from bs4 import BeautifulSoup

url = 'https://estate.ltn.com.tw/article/6814'
r = requests.get(url) #將此頁面的HTML GET下來
# print(r.text) #印出HTML
soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parser


# 新聞類
# h1 = soup.h1
# print('h1')
# print(h1.get_text())

content = soup.find("div", class_="page-name")
# print('content')
print(content.get_text().strip())


# 法條類
# content = soup.pre
# print(content.get_text().strip())