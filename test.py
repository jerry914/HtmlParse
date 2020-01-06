# import requests
# from bs4 import BeautifulSoup
# import json
# url = 'https://api.mediatek.com/mcs/v2/devices/DTRiZjmx/datachannels/temp/datapoints?limit=50'
# res = requests.get(url)

# soup = BeautifulSoup(res.text, 'html.parser')

# print(soup)

import urllib.request
import json
html = urllib.request.urlopen('https://api.mediatek.com/mcs/v2/devices/DTRiZjmx/datachannels/temp/datapoints?limit=50')
hjson = json.loads(html.read())
print(hjson['apiVersion'])

print(hjson['code'])