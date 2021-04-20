import requests
from bs4 import BeautifulSoup
import json

url='https://rent.591.com.tw/?kind=0&region=1'
r = requests.get(url)

soup = BeautifulSoup(r.text , 'html.parser')

houseCards = soup.select('.listInfo')

carousel = {
  "type": "carousel",
  "contents": [
    
  ]
}
count = 1
for houseInfo in houseCards :
    imgUrl = houseInfo.select('.imageBox img')[0].get('data-original')
    titleArea = houseInfo.select('.infoContent h3 a')[0]
    title = titleArea.text
    infoUrl = 'https:'+titleArea.get('href')

    bubble ={
      "type": "bubble",
      "direction": "ltr",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": title,
            "align": "center",
            "wrap": True,
            "contents": []
          }
        ]
      },
      "hero": {
        "type": "image",
        "url": imgUrl,
        "size": "full",
        "aspectRatio": "1.51:1",
        "aspectMode": "cover"
      },
      "footer": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "查看詳細",
              "uri": infoUrl
            }
          }
        ]
      }
    }
    if count < 13:
        carousel['contents'].append(bubble)
    else: 
        break

    count += 1
    



flexBox = {
  "type": "flex",
  "altText": "this is a flex message",
  "contents": carousel
}

f = open('house.json','w',encoding='utf-8')
f.write(json.dumps(carousel,ensure_ascii=False))
f.close()
print(flexBox)