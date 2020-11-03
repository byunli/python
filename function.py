from datetime import datetime
#def 函式名稱(參數):
#   要做的事情

# def sumCal(numberC,numberD):
#     result = numberC**numberD

#     return result

# print(sumCal(10,2))
def GetDatetime(formatDate):
    #formatDate 是 要轉換前的日期
    #分割字串取得年分
    tmpYear = formatDate.split("年")[0]
    #民國年轉換成西洋年
    nowYear = str(int(tmpYear)+1911)
    #分割字串取得月份
    tmpMonth = formatDate.split("年")[1]
    nowMonth = tmpMonth.split("月")[0]
    #組合字串供datetime.strptime()函數使用
    nowDate= nowYear+"/"+nowMonth+"/1"
    resultDate = datetime.strptime(nowDate,"%Y/%m/%d")
    return resultDate


print(GetDatetime("109年8月"))
print(GetDatetime("109年7月"))
