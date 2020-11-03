import requests
from bs4 import BeautifulSoup
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
# https://astro.click108.com.tw/daily_0.php?iAstro=0
# https://astro.click108.com.tw/daily_1.php?iAstro=1

astros = ["牡羊座","金牛座","雙子座","巨蟹座","獅子座","處女座",
            "天秤座","天蠍座","射手座","摩羯座","水瓶座","雙魚座"]

# for i in astros:
#     print(astros.index(i))

sumJ = []
while True:
    StringInput = input("請輸入要查詢的星座，若要離開請輸入Quit : ")
    if StringInput != "Quit":
        for i in astros:
            for j in i:
                if i == StringInput or j == StringInput or "座" == StringInput:
                    print("搜尋星座結果為:",i)
                    sum = astros[astros.index(i)]
                    url = "https://astro.click108.com.tw/daily_"+ str(astros.index(i)) + ".php?iAstro=" + str(astros.index(i))
                    r = requests.get(url)
                    soup = BeautifulSoup(r.text,'html.parser')
                    title = soup.select(".TODAY_CONTENT p")
                    print(astros[int(astros.index(i))])
                    for i in title:
                        print(i.text+"\n")
    else:
        print("Good-bye")
        break       