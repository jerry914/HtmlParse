import requests
from bs4 import BeautifulSoup
import os
import imgDownload
import bubbleDownload

rootUrl = 'https://sites.google.com/junyiacademy.org/linkit7697/'
route = 'getstart/基礎電學觀念'
url = rootUrl+route
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
fileRootPath = str('D:/workspace/HtmlParseBot/Linkit7697Learning Resources/')
imgfilePath = fileRootPath+'img/'+route+'/'
bubblefilePath = fileRootPath+'bubble/'+route+'/'

sectionBlock = soup.select("section")
sectionText = []
sectionImgCount = []
imgPath = []
imgIdx = 1
bubbleIdx = 1
for section in sectionBlock:
    if(section.text==''):
        continue
    img = section.find_all('img')
    if(section.select(".w536ob")):
        bubbleDownload.download_single_bubble(section.select(".w536ob"),bubblefilePath+'/'+str(bubbleIdx))
        bubbleIdx+=1
    
    sectionImgCount.append(len(img))
    for i in range(len(img)):
        # imgDownload.download_single_img(img[i]["src"],imgfilePath+'/'+str(imgIdx))
        imgIdx+=1
    
    sectionText.append(section.text)

i=0
for section in sectionText:
    print(sectionImgCount[i])
    print(section)
    i+=1


print("爬蟲結束")