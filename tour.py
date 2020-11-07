import requests
from bs4 import BeautifulSoup
import json


url = "https://www.taiwan.net.tw/m1.aspx?sNo=0001112"
r = requests.get(url)
# print(r.text)

# js 控制圖片的載入

# 將字串轉換成HTML格式，供套件操作
soup = BeautifulSoup(r.text, "html.parser")
# 利用select("CSS選擇器")進行網頁區塊提取
# card_imgs = soup.select(".graphic")
# card_titles = soup.select(".card-title")
# card_likes = soup.select(".target.target-like")
# 組合資料 len()檢查比數一樣多

# 最外圍所有的卡片被選中
cards = soup.select(".card")

saveData = {
    "data": [
        {
            "title": "標題",
            "img": "圖片連結",
            "like": "瀏覽人次"
        }
    ]
}

# 利用for迴圈遍歷cards
for card in cards:
    card_img = card.select(".graphic")[0].select(".noscriptImg")[0]["src"]
    card_title = card.select(".card-title")[0].text
    # .replace("\n"," ")
    card_like = card.select(".target.target-like")[0].text

    # 字典裝起來，格式較整齊
    tempData = {
        "title": card_title,
        "img": card_img,
        "like": card_like
    }
    # print(tempData)
    saveData["data"].append(tempData)

# print(saveData)

# 轉成json格式
jsonData = json.dumps(saveData,ensure_ascii=False)
print(jsonData)

# 將saveData存jason檔案
f = open("tour.json", "w", encoding="utf-8")
f.write(str(jsonData))
f.close()
