import requests
from datetime import datetime
# 參考網站
# https://opendata.cwb.gov.tw/dist/opendata-swagger.html#/%E9%A0%90%E5%A0%B1/get_v1_rest_datastore_F_C0032_001

r = requests.get(
    'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-7A389BFC-7466-4D46-9E71-FF4FDEB0EA46&format=JSON&locationName=')
weatherData = r.json()

for data in weatherData["records"]["location"]:
    print(data["locationName"], " - ", data["weatherElement"]
          [0]["time"][0]["parameter"]["parameterName"])
