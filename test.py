#coding=utf-8

dictData = {"data":{"result":{"limit":10,"offset":0,"count":821,"sort":"","results":[{"行政區":"士林區","編號":"1","備註":"中華汽車服務廠","地址":"士林區延平北路六段434號","_id":1,"單位":"中華汽車社子服務廠"},{"行政區":"士林區","編號":"2","備註":"公有停車場","地址":"士林區基河路150號","_id":2,"單位":"承德公園地下停車場"},{"行政區":"士林區","編號":"3","備註":"公有停車場","地址":"士林區中正路17號","_id":3,"單位":"福林公園地下停車場"},{"行政區":"士林區","編號":"4","備註":"車行","地址":"士林區文林路752號","_id":4,"單位":"瑞展機車商行"},{"行政區":"士林區","編號":"5","備註":"車行","地址":"士林區延平北路5段111號","_id":5,"單位":"金晉車業行"},{"行政區":"士林區","編號":"6","備註":"車行","地址":"士林區延平北路8段175號","_id":6,"單位":"得勝機車行"},{"行政區":"士林區","編號":"7","備註":"車行","地址":"士林區社中街462號","_id":7,"單位":"文發機車行"},{"行政區":"士林區","編號":"8","備註":"車行","地址":"士林區福港街268號","_id":8,"單位":"嘉榮機車行"},{"行政區":"士林區","編號":"9","備註":"車行","地址":"士林區德行東路206號","_id":9,"單位":"正大機車行"},{"行政區":"士林區","編號":"10","備註":"里辦公室","地址":"士林區延平北路7段107巷10號","_id":10,"單位":"福安里辦公室"}]}},"status":200,"statusText":"OK","headers":{"access-control-allow-headers":"X-Requested-With, Content-Type, Accept, Origin, Authorization","access-control-allow-methods":"GET, POST, PUT, DELETE, PATCH, OPTIONS","access-control-allow-origin":"*","cache-control":"no-store, no-cache, must-revalidate","connection":"keep-alive","content-length":"1468","content-security-policy":"frame-ancestors https://www.tgos.tw, frame-ancestors https://www.tgos.tw","content-type":"application/json","date":"Tue, 27 Oct 2020 06:00:44 GMT","expires":"Thu, 19 Nov 1981 08:52:00 GMT","pragma":"no-cache","server":"nginx","x-content-type-options":"nosniff, nosniff","x-frame-options":"SAMEORIGIN, SAMEORIGIN","x-xss-protection":"1;mode=block, 1;mode=block"},"config":{"transformRequest":{},"transformResponse":{},"timeout":0,"xsrfCookieName":"XSRF-TOKEN","xsrfHeaderName":"X-XSRF-TOKEN","maxContentLength":-1,"headers":{"Accept":"application/json, text/plain, */*"},"method":"get","params":{"q":"","limit":"10","offset":""},"url":"/api/v1/dataset/c2b666e0-f848-4609-90cb-5e416435b93a?scope=resourceAquire"},"request":{}}

# # print(dictData)
# print(dictData["data"]["result"]["results"][1]["單位"])
# print(type(dictData["data"]["result"]["limit"]))

# for i in range(dictData["data"]["result"]["limit"]):
#     print(dictData["data"]["result"]["results"][i]["單位"]," - ",dictData["data"]["result"]["results"][i]["地址"])
    
# for i in range(len(dictData["data"]["result"]["results"])):
#     print(dictData["data"]["result"]["results"][i]["單位"]," - ",dictData["data"]["result"]["results"][i]["地址"])

# 取值
# for data in dictData["data"]["result"]["results"]:
#     print(data["單位"]," - ", data["地址"],"\n")

# dictData = {"data":[
#     {"name":"john","age":18},
#     {"name":"alex","age":19}
# ]}

# # 修改
# dictData["data"][1]["age"] = 20
# print(dictData["data"][1]["age"])
# print(dictData)

# #新增16歲的jack
# dictData["data"].append({"name":"jack","age":16})
# # print(dictData["data"])

#新增性別項目
# dictData["data"][0]["gender"] = "male"
# dictData["data"][1]["gender"] = "male"
# dictData["data"][2]["gender"] = "male"
# print(dictData)

# for i in dictData["data"]:
#     # print(i)
#     i["gender"] = "male"

#------------------------------------------
# #把john刪掉
# del dictData["data"][0]
# # #是list因為中括號(索引值)
# # dictData["data"].pop(0)

# #把age刪掉
# for i in dictData["data"]:
#     # print(i)
#     del i["age"]
# print(dictData["data"])

