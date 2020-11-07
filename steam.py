import requests
from bs4 import BeautifulSoup
import json

url = "https://store.steampowered.com/search/?term="

# 換語系
headers = {
    "Accept-Language":"zh-TW"
    # "Accept-Language":"zh-TW,zh;q=0.9,en-US;q=0.8"

}

r = requests.get(url,headers=headers)
soup = BeautifulSoup(r.text,"html.parser")
games = soup.select(".search_result_row")
# print(games)

gameData = {
    "games":[]
}

# 一個一個遊戲
for game in games:
    # 抓到每個遊戲的src
    img = game.select("img")[0].get("src")
    title = game.select(".title")[0].text
    release = game.select(".search_released")[0].text
    price = game.select(".search_price")[0].text.replace(" ","").replace("\r","").replace("\n","")
    print(price)

    tmpData = {
        "title":title,
        "img":img,
        "release":release,
        "price":price
    }
    gameData["games"].append(tmpData)

# 存字典格式
# print(gameData)

jsonData = json.dumps(gameData,ensure_ascii=False)

f = open("steam_game.json","w",encoding="utf-8")
f.write(str(jsonData))
f.close()





