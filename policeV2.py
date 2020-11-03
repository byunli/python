# coding=utf-8
# 臺北市道路交通事故按月別
import requests
from datetime import datetime

def GetDatetime(formatDate,plus=0):
    #formatDate 是 要轉換前的日期
    #分割字串取得年分
    tmpYear = formatDate.split("年")[0]
    #民國年轉換成西洋年
    nowYear = str(int(tmpYear)+1911+plus)
    #分割字串取得月份
    tmpMonth = formatDate.split("年")[1]
    nowMonth = tmpMonth.split("月")[0]
    #組合字串供datetime.strptime()函數使用
    nowDate= nowYear+"/"+nowMonth+"/1"
    resultDate = datetime.strptime(nowDate,"%Y/%m/%d")
    return resultDate

# 1. 請列出每月交通事故的件數
#    請列出每月交通事故造成的死亡人數
    #tips: 先利用api參數limit限制讀取的資料筆數
    #      再利用較少的資料觀察資料的格式
#利用requests.get()函式，取得網址回傳的資料。
r = requests.get('https://data.taipei/api/v1/dataset/89027714-a61a-485d-9abc-b8fca186e9fc?scope=resourceAquire')
# #json()函式，將資料從字串轉換為dict可操作的格式
policeData = r.json()
# print(policeData)

# #觀察資料格式，取得某月交通事故件數
# print(policeData["result"]["results"][0]["發生件數[件]"])

# for data in policeData["result"]["results"]:
#     print(data["年月別"],":\n\t交通事故發生件數",data["發生件數[件]"],"件\n\t交通事故造成死亡人數:",data["死亡人數[人]"],"人")

# 2. 請列出每年交通事故的件數
#    請列出每年交通事故造成的死亡人數
    #tips: 如何利用時間函式進行範圍限制

#讀出第一筆資料的年份
#儲存第一筆資料的年份
#件數變數儲存當年每月的件數
# chkYear = ''
# # 發生件數
# count = 0
# # 死亡人數
# death = 0
# for data in policeData["result"]["results"]:
#     # 分割字串，分離出當下的年份為何
#     nowYear = data["年月別"].split("年")[0]
#     # 確認當下年分與儲存的年份是否相等
#     if chkYear == nowYear:
#         count += int(data["發生件數[件]"])
#         death += int(data["死亡人數[人]"])
#     #換年份
#     else :
#         if chkYear :
#             print(chkYear,"年:\n\t交通事故件數為:",count,"件\n\t交通事故死亡人數為:",death,"人")
#         chkYear = nowYear
#         count=int(data["發生件數[件]"])
#         death=int(data["死亡人數[人]"])

# 3. 取得近十年每個月交通事故件數的平均
    #tips: 利用時間函式過濾出近10年資料，加總平均

#最後一筆資料往前回推十年  97/08-107/08

# 1. 利用串列特性取得最後一筆資料的年月別
#取得最後一筆資料
lastData= policeData["result"]["results"][-1]

#利用GetDatetime的自製函式，進行時間格式轉換
lastDate = GetDatetime(lastData["年月別"])
firstDate = GetDatetime(lastData["年月別"],-10)
print("lastDate",lastDate)
print("firstDate",firstDate)

# 4. 利用迴圈遍歷取得的資料
countCase = 0
countMonth = 0
for data in policeData["result"]["results"]:
    # 5. 將每筆資料的年月別取出，轉換成datetime型別
    nowDate = GetDatetime(data["年月別"])
    print("nowDate",nowDate)
    #如果 現在時間>起始時間 以及 現在時間小於結束時間
    # 6. 利用datetime型別特性進行時間比較
    if nowDate>firstDate and nowDate<=lastDate:
        # 7. 判斷符合時間內的資料進行累加
        countCase+= int(data["發生件數[件]"])
        countMonth+=1
# 8. 迴圈結束後將十年間件數總數除以十年間資料筆數
print(countCase)
print(countMonth)
# 9. 輸出答案至畫面
print(countCase/countMonth)

# 4. 請找出交通事故發生件數最高的年月別(取三個月)
    #tips: 如何利用dict進行排序

