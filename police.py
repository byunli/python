# coding=utf-8
# 臺北市道路交通事故按月別
import requests
from datetime import datetime
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
#將年月別進行分割，保留年份至lastYear
lastYear = lastData["年月別"].split("年")[0]
#將年月別進行分割，保留月份至lastMonth
lastMonth =lastData["年月別"].split("年")[1]
lastMonth = lastMonth.split("月")[0]
# 2. 計算出最後一筆資料往回推10年的年月別
firstYear= int(lastYear)-10
firstMonth = lastMonth
# 3. 利用時間函數將起點時間與終點時間，轉換成datetime型別
# 組合最後年月日
tmpDate = str(int(lastYear)+1911)+"/"+lastMonth+"/1"
# 利用datetime.strptime()函式，
# 將tmpDate轉換成datetime型別，儲存至lastDate
lastDate = datetime.strptime(tmpDate,"%Y/%m/%d")
# 組合起始年月日
tmpDate = str(firstYear+1911)+"/"+firstMonth+"/1"
# 利用datetime.strptime()函式，
# 將tmpDate轉換成datetime型別，儲存至firstDate
firstDate = datetime.strptime(tmpDate,"%Y/%m/%d")
# 4. 利用迴圈遍歷取得的資料
countCase = 0
countMonth = 0
for data in policeData["result"]["results"]:
    # 5. 將每筆資料的年月別取出，轉換成datetime型別
    nowYear = data["年月別"].split("年")[0]
    nowMonth = data["年月別"].split("年")[1]
    nowMonth = nowMonth.split("月")[0]
    tmpDate = str(int(nowYear)+1911)+"/"+nowMonth+"/1"
    nowDate = datetime.strptime(tmpDate,"%Y/%m/%d")

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




x = "87年1月"
#利用年字進行字串分割
xSplit = x.split("年")
# print("xSplit:",xSplit)
# #將民國年轉換成西洋年
# year = int(xSplit[0])+1911
# print("year",year)
# #將該年年分與1/1重組成字串
# currentDate = str(year)+"/1/1"
# print(currentDate,type(print(currentDate)))
# #將時間的字串轉換成時間格式
# currentDate = datetime.strptime(currentDate,"%Y/%m/%d")
# print(currentDate,type(print(currentDate)))
# 每年1/1 00:00:00 - 1/1 00:00:00