import requests
from bs4 import BeautifulSoup
import os
from opencc import OpenCC
cc = OpenCC('s2twp')


f = open("D:/workspace/HtmlParseBot/HtmlParse/output/raspberrypilearning/pathList.txt", "r",encoding = 'utf8')
for x in f:
    print(x)
    projectName = x.replace("\n",'')
    try:
        os.mkdir("D:/workspace/HtmlParseBot/Code Club-Learning Resources/"+projectName+"/zh-TW")
        stepIdx = 1
        while 1:
            # projectName = 'happy-birthday'
            step = stepIdx
            url = 'https://raw.githubusercontent.com/raspberrypilearning/'+projectName+'/master/zh-CN/step_'+str(step)+'.md'
            resp = requests.get(url)
            # print(resp.text)
            if resp.status_code == 200:
                resp = requests.get(url)
                conText = resp.text
                conText = cc.convert(conText)
                with open("D:/workspace/HtmlParseBot/Code Club-Learning Resources/"+projectName+"/zh-TW/step_"+str(step)+".md", 'w',encoding = 'utf8') as f: 
                    f.write(conText)
                    f.close()
                stepIdx+=1
            else:
                break
    except Exception as e:
        print(e)