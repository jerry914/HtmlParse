import requests
from bs4 import BeautifulSoup
import os


rootUrl = 'https://sites.google.com/junyiacademy.org/linkit7697/'
route = 'getstart/基礎電學觀念'
url = rootUrl+route
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
fileRootPath = str('D:/workspace/HtmlParseBot/Linkit7697Learning Resources/img/')
filePath = fileRootPath+route


sectionBlock = soup.find_all('section')
imgBlock = soup.find_all('small')
for d in sectionBlock:
    print(d.get_text())
    try: 
        img = d.find_all('img')
        imgText = d.find_all('small')
        for i in range(len(img)):
            print(imgText[i].text)
            print(img[i]["src"])
            pic=requests.get(img[i]["src"])
            img2 = pic.content
            pic_out = open(filePath+'/'+str(imgText[i].text)+".png",'wb')
            pic_out.write(img2)
            pic_out.close()
    except Exception as e:
        print(e)

# https://jerry914.github.io/Linkit7697Learning-Resources/img/DIR.png


print("爬蟲結束")