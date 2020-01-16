import requests
from bs4 import BeautifulSoup
url = 'https://zh.wikipedia.org/wiki/%E6%A4%8D%E7%89%A9#保護'
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')

print(soup.text)
sectionBlock = soup.select("p")
sectionText = []

for section in sectionBlock:
    if(section.text==''):
        continue
    else:
        sectionText.append(section.text)
print(sectionText)

# import urllib.request
# import json
# html = urllib.request.urlopen('https://api.mediatek.com/mcs/v2/devices/DTRiZjmx/datachannels/temp/datapoints?limit=50')
# hjson = json.loads(html.read())
# print(hjson['apiVersion'])

# print(hjson['code'])