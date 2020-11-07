import requests
from bs4 import BeautifulSoup
import json

url ="https://rent.591.com.tw/?kind=0&region=1"
r = requests.get(url)
# 將html字串轉換為可操作格式
soup = BeautifulSoup(r.text,"html.parser")
# 選取房子區塊
houseArea = soup.select(".listInfo.clearfix")

# 預設資料格式
houseData = {
    "house":[]
}

# 遍歷房子資料
for data in houseArea:
    # 利用解構將房屋資訊分別儲存
    info,address,detail = data.select("li > p")\
    # 利用replace清除不要的雜訊
    newInfo = info.text.replace(" ","").replace("\n","").replace("\xa0","")
    # 利用split切開資訊
    info = newInfo.split("|") 
    rooms=""
    if len(info) == 3:
        type,ping,floor =newInfo.split("|") 
    else:
        type,rooms,ping,floor=newInfo.split("|") 

    # 將單筆房屋資訊整理成字典
    save = {
        "title":data.select("h3 a")[0].text,
        "type":type,
        "rooms":rooms,
        "ping":ping,
        "floor":floor,
        "address":address.text.replace("\n","").replace(" ",""),
        "price":data.select(".price")[0].text.replace("\n","").replace(" ","")
    }
    # 將單筆資訊存入houseData
    houseData["house"].append(save)
    
# 將整理好的資料轉換成JSON格式
jsonData = json.dumps(houseData,ensure_ascii=False)

# 存檔
fp = open("house.json","w",encoding="utf-8")
fp.write(jsonData)
fp.close()

