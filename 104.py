import requests
from bs4 import BeautifulSoup
import json

url = "https://www.104.com.tw/jobs/search/?keyword=Python"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
}
r = requests.get(url,headers=headers)

soup = BeautifulSoup(r.text,"html.parser")
# 在固定範圍內搜尋指定資料
pages = soup.find("script", text=lambda text: text and "totalPage" in text) 
# print(pages)

#神奇刀工，去頭去尾
firstSplit = str(pages).split("    var initFilter = ")
# print(firstSplit[1])
secondSplit =  firstSplit[1].split(";\n    var staticPath = ")
# print(secondSplit[0])

jsonData = json.loads(secondSplit[0])

ret = json.dumps(jsonData, ensure_ascii=False)

fp = open('job.json',mode='w',encoding='utf-8')
fp.write(ret)

# print(str(pages).split("var initFilter = ")[1].split("\n    var staticPath =")[0])
# jobs =soup.select(".js-job-link")

# print(len(jobs))
# for job in jobs:
#     print(job.text)

# ret = json.dumps(newsDict, ensure_ascii=False)
# fp = open('out.json',mode='w',encoding='utf-8')
# fp.write(ret)
