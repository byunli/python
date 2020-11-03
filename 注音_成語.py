# 成語接龍
# api 

# 這個API是字典，不是成語字典
# - 成語至少要四個字，需要過濾四個字以下的詞彙

# 觀察出沒資料與有資料的資料結構
# - 判斷出若無heteronyms則沒資料
# - 取得資料需透過heteronyms[0]

import requests
# # # 串上api測試
# url = 'https://www.moedict.tw/pua/一飛沖天'
# r = requests.get(url)
# data = r.json()




# ----------------------------------------------
# 如何利用相同注音接龍

idiom = ""
last_bopomofo=[]
while True:
    #接收玩家的輸入資料
    print("目前成語:",idiom)
    player = input("請輸入一個成語:")

    if player == "end":
        print("謝謝遊玩")
        break
    if player == "clear":
        idiom=""
        continue
    
    # 判斷是否少於四個字
    if len(player) < 4:
        print("請輸入正確的成語")
        continue
    
    # 將玩家輸入的字組合API並撈取資料
    url = "https://www.moedict.tw/pua/" + player
    r = requests.get(url)
    data = r.json()
    #利用字典API判斷是否為成語
    if data.get("heteronyms") == None :
        print("請輸入正確的成語")
        continue

    #判斷是否有儲存過成語
    
    if idiom :
        # 判斷第一個字是否與前一個詞彙最後一個字相等
        # 把字串分割
        listIdiom = list(idiom)
        listPlayer = list(player)

        # 玩家輸入的注音，取最後一個注音
        bopomofo = data.get("heteronyms")[0]["bopomofo"]
        first_bopomofo = bopomofo.split(" ")[0]   
        print("first_bopomofo = ",first_bopomofo)     

        if(first_bopomofo == last_bopomofo):
            idiom = player
        else:
            print("接龍失敗，請回去重新輸入")
    else: 
        idiom = player
        bopomofo = data.get("heteronyms")[0]["bopomofo"]
        last_bopomofo = bopomofo.split(" ")[-1]
        print("last_bopomofo = ",last_bopomofo)
        print("把成語存下來")










