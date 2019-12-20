import requests
from bs4 import BeautifulSoup
import os


def download_single_bubble(d,filePath):
    try: 
        domIdx = str(d).find("&lt;!DOCTYPE")
        domEnd = str(d).find("&lt;/html&gt;")
        content = str(d)[domIdx:domEnd]+"&lt;/html&gt;"
        content = content.replace("&lt;","<")
        content = content.replace("&gt;",">")
        print(content)
        html_out = open(filePath+".html",'w',encoding = 'utf8')
        html_out.write(content)
        html_out.close()
    except Exception as e:
        print(e)

# https://jerry914.github.io/Linkit7697Learning-Resources/bubble/DIR.html

print("bubble Dowmload !")