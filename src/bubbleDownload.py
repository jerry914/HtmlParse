import requests
from bs4 import BeautifulSoup
import os


rootUrl = 'https://sites.google.com/junyiacademy.org/linkit7697/'
route = 'getstart/基礎電學觀念'
url = rootUrl+route
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
fileRootPath = str('D:/workspace/HtmlParseBot/Linkit7697Learning Resources/bubble/')
filePath = fileRootPath+route


sectionBlock = soup.select(".w536ob")
idx=1
for d in sectionBlock:
    # print(d)
    try: 
        domIdx = str(d).find("&lt;!DOCTYPE")
        domEnd = str(d).find("&lt;/html&gt;")
        
        content = str(d)[domIdx:domEnd]+"&lt;/html&gt;"
        content = content.replace("&lt;","<")
        content = content.replace("&gt;",">")
        print(content)
        html_out = open(filePath+'/'+str(idx)+".html",'w',encoding = 'utf8')
        html_out.write(content)
        html_out.close()
        idx+=1
    except Exception as e:
        print(e)

# https://jerry914.github.io/Linkit7697Learning-Resources/bubble/DIR.html

print("爬蟲結束")