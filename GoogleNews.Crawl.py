import requests
from bs4 import BeautifulSoup

url = "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFZxYUdjU0JYcG9MVlJYR2dKVVZ5Z0FQAQ?hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant"
r = requests.get(url)
soup = BeautifulSoup(r.text,"html.parser")

# .DYST1d

title = soup.select(".VDXfz")
media = soup.select(" MQsxIb xTewfe R7GTQ keNKEd j7vNaf Cc0Z5d EjqUne)

for data in media:
    print(data)

# for i,v in enumerate(title):
#     print(media[i].text," - ",)
