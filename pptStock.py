import requests
from bs4 import BeautifulSoup
r = requests.get("https://www.ptt.cc/bbs/Stock/index.html")
soup = BeautifulSoup(r.text,'html.parser')
# print(soup.prettify())
# print(soup.find_all(class_="title"))

# for a in soup.find_all('a'):
#     print(a.text)
# for title in soup.find_all('div','title'):
#     print(title.a.text)


# 撈出標題--------------------
title = soup.select(".title a")
for i in title:
    print(i.text)

for posts in soup.find_all('div','title'):
    for post in posts.stripped_strings:
        print(post)
# ----------------------------



