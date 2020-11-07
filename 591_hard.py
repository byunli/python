import requests
from bs4 import BeautifulSoup
import json

url ="https://rent.591.com.tw/home/search/rsList?is_new_list=1&type=1&kind=0&searchtype=1&region=1&firstRow=30&totalRows=13509"
#如何在送出請求時，將cookies一併送出
cookies={
    "591_new_session":"eyJpdiI6IklSS004d01EWElTRk1BanhncFNkRUE9PSIsInZhbHVlIjoiMFBuTjZjajZBcmxcL3F6QTZNclU4aUdVVHE2aWVMUXVhYyswdTlLeE1Ma1NOMGdIeVhrUGJQVHRYMFIxUnUrVk1cL2Z0a1JQWUdRN2YzWVljWlJpdUVzQT09IiwibWFjIjoiOWEzNjBkYTVhYWNkNmZiNzRlMzNiZWJjOWI2NmUzNTJkOGFmNmFkYWUxYzMzM2MwZWMyOGEyYTEwZjUwODQzNCJ9"
}
headers ={
"Host": "rent.591.com.tw",
"Connection": "keep-alive",
"Accept": "application/json, text/javascript, */*; q=0.01",
"X-CSRF-TOKEN": "h0uujIOcelXWUBoMiHIVAkKAKnJmRPEnNeChu3em",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
"X-Requested-With": "XMLHttpRequest",
"Sec-Fetch-Site": "same-origin",
"Sec-Fetch-Mode": "cors",
"Sec-Fetch-Dest": "empty",
"Referer": "https://rent.591.com.tw/?kind=0&region=1",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
"Cookie": "webp=1; XSRF-TOKEN=eyJpdiI6IlVlTE9Eb21helA3R1lVY2JGOXRZQWc9PSIsInZhbHVlIjoiSG9hUjdoNjBpQWZtQ3RiMVZcLzNQQXBhWTdMSWpFNnN3MGVoSmVFTzR6YW11WVVJRkFXR05tVUtrR21iaE94bmlINzcrNlJFWG9zaHlHZk1ObmNaZG53PT0iLCJtYWMiOiJiN2Q1NjBiYzE5ZTFhNDg4MWY5MTI1NTlkOGFmNDc3MTZiMGNiNjcxNjc0YThlZjg0MDk5NTU0YjU4ZmEyYTBkIn0%3D; 591_new_session=eyJpdiI6Ik1kRFBOZGx0SnZWbE1DTEtNdVprMUE9PSIsInZhbHVlIjoicEhkZGZzbDRSOWZoK0wwNXZKV3hGdUlVdVRSYlNPeko3QVlqSVBXeDNRM0YwK1FPanhcL29JMkk1UWVBODh1blNnWFNubWd1RWtFc0gwMWpRa1oyQWdBPT0iLCJtYWMiOiI2N2ZkN2YwMmM3OWQ0NWRiYjFjNjA3OTJlZTg2MDE4NDYwYzI5Yjk2ZDc1OGI2YmNjNmE3OGI1ZDQ0OWNjMGNjIn0%3D",
}
r = requests.get(url,cookies=cookies,headers=headers)
# print(r,r.json())

fp = open("house1.json","w",encoding="utf-8")
fp.write(str(r.json()))
fp.close()