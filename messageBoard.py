import requests
import time
from datetime import datetime

while True:
    text = input("請輸入留言:")
    my_data = {
    "title":"test",
    "content":text,
    "date":"2020/10/30",
    }
    r = requests.post('https://ajax-lesson.digipack-develop.com/news?limit=3',data = my_data)
    # print(r.text) 
    # success

    r = requests.get('https://ajax-lesson.digipack-develop.com/news?limit=10')
    messageData = r.json()
    # 標題、時間、內文
    # count = 0
    for message in messageData:
        # count += 1

        print("-"*30)
        print("title:",message["title"])
        print("date:",message["date"])
        print("content:",message["content"])
        # if count == 20:
        #     break
    time.sleep(3)






