from bs4 import BeautifulSoup
from flask import Flask, request
import requests
import json
app = Flask(__name__)


@app.route('/')
def news():

    url = "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFZxYUdjU0JYcG9MVlJYR2dKVVZ5Z0FQAQ?hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant"
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser")
    # 取得頭條新聞的，標題區塊
    titleArea = soup.select('.MQsxIb.xTewfe.R7GTQ.keNKEd.j7vNaf.Cc0Z5d.EjqUne')

    newsDict = {}
    # enumerate() 枚舉
    # lisrData = [5,6,4,32,3]
    # print(list(enumerate(lisrData)))
    for v in enumerate(titleArea):
        title = v.select(".DY5T1d")[0].text
        media = v.select(".wEwyrc.AVN2gc.uQIVzc.Sksgp")[0].text
        url = "https://news.google.com/" + v.select(".DY5T1d")[0].get("href")
        content = v.select('.xBbh9')[0].text if len(v.select('.xBbh9')) else ""
        #如果Key不存在則新增一個Key值為空串列
        if newsDict.get(media) == None :
            newsDict[media] = [] 
        dataDict = {
            "title":title,
            "href":url,
            "content":content
        }
        newsDict[media].append(dataDict) 

    ret = json.dumps(newsDict, ensure_ascii=False)

    return ret


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)

