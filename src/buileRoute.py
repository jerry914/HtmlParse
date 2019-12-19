import requests
from bs4 import BeautifulSoup
import json
import marko
import os

def get_tag_text(url,tag):
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp, 'html.parser')
            return soup.find(tag).text
    except Exception as e:
        print('Exception: %s' %(e))
        return None
rooturl = 'https://sites.google.com/junyiacademy.org/linkit7697'
url = 'https://sites.google.com/junyiacademy.org/linkit7697/getstart/%E5%9F%BA%E7%A4%8E%E9%9B%BB%E5%AD%B8%E8%A7%80%E5%BF%B5'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
# filePath = str(FILEPATH)


pathData = soup.select("a")
# print(pathData)

for d in pathData:
    # print(d['href'])
    # print(d.text)
    try: 
        path = d['href']
        if(path.find("linkit7697")==18):
            path = path.replace("/junyiacademy.org/linkit7697/","")
            print(path)
            if not os.path.isdir(path):
                os.mkdir(path)
    except Exception as e:
        print(e)

print("爬蟲結束")