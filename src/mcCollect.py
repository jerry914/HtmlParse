import requests
from bs4 import BeautifulSoup
import os
import junyiJSONgenerate
import re


projectName = 'block-out'
url = "https://arcade.makecode.com/lessons/"+projectName
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')
content = soup.text
pointer = 0


codeBlock = soup.find_all("code", class_="lang-blocks")

sctIdx = 0
for b in codeBlock:
    sctIdx+=1
    sct = str(b.text)
    with open("D:/workspace/arcade-test/"+projectName+"/"+str(sctIdx)+".html", 'w',encoding = 'utf8') as f: 
        f.write(junyiJSONgenerate.JSON_open("src/Templete/script").replace("SCRIPT",sct))
        f.close()

junyiJSONgenerate.JSON_write(content,"output/makecode/"+projectName)

# part = content.split("Part")
# partIdx = 0
# for p in part:
#     junyiJSONgenerate.JSON_write(p,"output/makecode/"+projectName+p[:3].replace("\n",""))
#     # junyiJSONgenerate.JSON_write(p,"output/makecode/"+str(partIdx))
#     partIdx +=1



