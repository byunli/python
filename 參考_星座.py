import requests
from bs4 import BeautifulSoup
# 製作一個串列裝所有可輸入的星座代號
# astros = ["牡羊座","金牛座","雙子座","巨蟹座","獅子座","處女座","天秤座","天蠍座","射手座","摩羯座","水瓶座","雙魚座"]

astrosDict = {"牡羊座":"0","金牛座":"1","雙子座":"2","巨蟹座":"3","獅子座":"4","處女座":"5","天秤座":"6","天蠍座":"7","射手座":"8","摩羯座":"9","水瓶座":"10","雙魚座":"11"}
# 組合字串，並印出所有可選星座
# text = ''
# for index,value in enumerate(astros):
#     text += value+":"+str(index)+" "
# print(text)

# 儲存使用者輸入之星座
astrosInput = input("請輸入欲查詢的星座名稱:")

# 將使用者輸入之數字結合網址，並送出請求取得網頁
# 透過觀察得知
# 網址的daily_0 iAstro=0 數字與星座相關
# 讓使用者輸入星座
url = "https://astro.click108.com.tw/daily_"+astrosDict[astrosInput]+".php?iAstro="+astrosDict[astrosInput]
r = requests.get(url)
# 將回傳之網頁HTML轉換為可操作格式
soup = BeautifulSoup(r.text, 'html.parser')

# 利用選擇器，選取到今日整體運勢
data = soup.select(".TODAY_CONTENT > p")

# 印出今日星座運勢
print("\n"+astrosInput+"今日的整體運勢為:\n")
print(data[0].text)
print(data[1].text)




# astros[0]="牡羊座";
# astros[1]="金牛座";
# astros[2]="雙子座";
# astros[3]="巨蟹座";
# astros[4]="獅子座";
# astros[5]="處女座";
# astros[6]="天秤座";
# astros[7]="天蠍座";
# astros[8]="射手座";
# astros[9]="摩羯座";
# astros[10]="水瓶座";
# astros[11]="雙魚座";
