import requests
from datetime import datetime, date, timedelta
from bs4 import BeautifulSoup

resp = requests.get('https://data.taipei/api/v1/dataset/b0011e96-3fc3-43ec-8bf5-07fb46dd22bb?scope=resourceAquire')

dictData = resp.json()

# 取得今天日期
today = date.today()
# print('今天的日期: ',today)
# print('-'*30)

# 取得今天的年份和月份
month = today.month
year = today.year

nextMonth = month + 1
currentYear = year 

if month == 12:
    nextMonth = 1
    currentYear += 1
# print(currentYear,'/', nextMonth)

star = str(currentYear)+'/'+str(nextMonth)+'/01'
end = str(currentYear)+'/'+str(nextMonth+1)+'/01'

# 判斷這個日期是否在2020年11月
startDate = datetime.strptime(star, '%Y/%m/%d')
endDate = datetime.strptime(end, '%Y/%m/%d')

# 取值11月放假的日期
for data in dictData["result"]["results"]:
    formatDate =  datetime.strptime(data["date"], '%Y/%m/%d')
    # ddd = date.fromisoformat(data["date"])
    if formatDate >= startDate and formatDate < endDate:
        print(data["date"]," - ", data["holidayCategory"], " - ", data["name"])


# print(soup)
# print(soup.h1.text)

# for title in soup.find_all('h3','post-title'):
#     print(title)
#     print(title.text)

# for h3 in soup.find_all('h3'):
#     print(h3.a)


# for posts in soup.find_all('div','post-body'):
#     for post in posts.stripped_strings:
#         print(post)