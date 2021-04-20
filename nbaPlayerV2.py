import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json
url = "https://www.basketball-reference.com/players/a/"
r = requests.get(url)
soup = BeautifulSoup(r.text,"html.parser")

#資料格式
dataFormat ={
    "players":[]
}  


#選擇網頁內的table > tbody > tr
players = soup.select("#players tbody tr")

for player in players:
    # 取得球員姓名
    name = player.select('[data-stat="player"]')[0].text
    # 利用表格特性，解構除了姓名外的所有資料
    from_ ,to ,position,height,weight,birthday,college = player.select('td')
    
    # 利用時間函式重組日期資料
    birthday = birthday.get("csk")
    if birthday :
        birthdayFormat = datetime.strptime(birthday,"%Y%m%d")
        birthday = datetime.strftime(birthdayFormat,"%Y/%m/%d")
    # 計算身高
    height = height.get("csk")
    if height:
        height = round(float(height)*2.54,2)
    # 計算體重
    weight = weight.text
    if weight:
        weight = round(float(weight)*0.45359237,2)
    
    # 組合資料
    tmpData = {
        "name":name,
        "from":from_.text,
        "to":to.text,
        "position":position.text.split('-'),
        "height":height,
        "weight":weight,
        "birthday":birthday,
        "college":college.text.split(",")
    }
    # 儲存資料至字典
    dataFormat["players"].append(tmpData)

# 字典傳換成JSON格式
jsonData = json.dumps(dataFormat,ensure_ascii=False)

# 儲存成檔案
f = open("nba.json","w",encoding="utf-8") 
f.write(jsonData)
f.close()

