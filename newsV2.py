import requests
from bs4 import BeautifulSoup
import json
from io import StringIO

url = "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFZxYUdjU0JYcG9MVlJYR2dKVVZ5Z0FQAQ?hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant"
r = requests.get(url)
soup = BeautifulSoup(r.text,"html.parser")
# 取得頭條新聞的，標題區塊
titleArea = soup.select('.MQsxIb.xTewfe.R7GTQ.keNKEd.j7vNaf.Cc0Z5d.EjqUne')

# print(titleArea)
# tag -> div
# id -> #id名稱
# class -> .class名稱
#   test = soup.select(".ekueJc.RD0gLb")
#   同一標籤上的class可以疊加在一起，中間不要間隔，
#   就可以過濾其他不符合的標籤

# 屬性選擇器 -> [attr=value]
#   titleArea = soup.select('[jsname="jVqMGc"]')

# 狀態選擇器 -> a:active , a:visited , a:checked

# 直屬選擇器 -> >
#   只能往內選一層

# 後代選擇器 ->  空白間隔
#   test = soup.select(".ipQwMb.ekueJc.RD0gLb a")

# 通用同層選擇器 -> ~
#   僅向下尋找，不會往上找同層符合的對象
#   test = soup.select(".ipQwMb.ekueJc.RD0gLb ~ div")

# 鄰接同層選擇器 -> +
#   僅向下尋找一個相鄰同層的對象
#   test = soup.select(".ipQwMb.ekueJc.RD0gLb + div")


newsDict = {}
# enumerate() 枚舉
# lisrData = [5,6,4,32,3]
# print(list(enumerate(lisrData)))
for i,v in enumerate(titleArea):
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

print(newsDict)

ret = json.dumps(newsDict, ensure_ascii=False)
print(ret)

fp = open('out.json',mode='w',encoding='utf-8')
fp.write(ret)

# 怎麼寫一隻檔案(讀取檔案、寫入資料)
# dict轉換成json

# json轉換預設會將中文傳成ascii
# 如何避免寫入時的亂碼

# data = {'today': 8, 'is': 6, 'nice': 8, 'day': 6}
# output = json.dumps(data)
# print(output)
# print(data , type(data))

# f = open('test.json','w')
# f.write(output)
# f.close()




        





# print()
# title = soup.select('.DY5T1d')
# media = soup.select('.wEwyrc.AVN2gc.uQIVzc.Sksgp')
# content = soup.select('.xBbh9')
# img = soup.select('.tvs3Id.QwxBBf')
# new_url = "https://news.google.com/stories/"

# mediaDict = dict()
# for i,v in enumerate(title):
#     mediaName = media[i].text
#     if mediaDict.get(mediaName) == None :
#         mediaDict[mediaName]=[]

#     newsDetail = {
#         "title":v.text,
#         "content":content[i].text,
#         "href":new_url+v.get("href"),
#         "img":img[i].text
#     }
    
#     mediaDict[mediaName].append(newsDetail)

# print(mediaDict)
