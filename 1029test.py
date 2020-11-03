import requests
from datetime import datetime, date, timedelta
from bs4 import BeautifulSoup

resp = requests.get('https://data.taipei/api/v1/dataset/89027714-a61a-485d-9abc-b8fca186e9fc?scope=resourceAquire')
dictData = resp.json()

for data in dictData["result"]["results"]:
    nowYear = data["年月別"].split("年")[0]
    nowMonth = data["年月別"].split("年")[1]
    nowMonth = nowMonth.split("月")[0]
    tmpData = str(int(nowYear))


# 請列出每月交通事故的件數
# 請列出每月交通事故造成的死亡人數
# 取日期，存交通事件數

# for data in dictData["result"]["results"]:
#     # 87年1月
#     month = data["年月別"]
#     event = int(data["發生件數[件]"])
#     death = int(data["死亡人數[人]"])
#     print(month,"-",event,"-",death)

# 1911
# 列出每年交通事故
x = '87年1月'
xSplit = x.split('年')
year = int(xSplit[0])+1911
print(year)
# month = xSplit[1].split['月'][0]
# print(int(month))
startDate = str(year)+"/1/1"
endDate = str(year)+"/12/1"

# startDate = datetime.strptime(star, '%Y/%m/%d')
# endDate = datetime.strptime(end, '%Y/%m/%d')

# 平均近十年每月交通事故的件數
# 請列出每年交通事故的件數
# 請列出每年交通事故造成的死亡人數

for data in dictData["result"]["results"]:
    currentDate = datetime.strptime(currentDate, '%Y/%m/%d')
    print(type(currentDate))
    


