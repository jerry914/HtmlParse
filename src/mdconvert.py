import marko
import requests
from bs4 import BeautifulSoup
import junyiJSONgenerate
import exportCSV
import imgDownload
import os
import re

from googletrans import Translator
translator = Translator()
# from opencc import OpenCC
# cc = OpenCC('s2twp')

def get_tag_text(url,tag):
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            mark = marko.convert(resp.text)
            soup = BeautifulSoup(mark, 'html.parser')
            return soup.find(tag).text
    except Exception as e:
        print('Exception: %s' %(e))
        return None
def get_tag(url,tag):
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            # mark = marko.convert(resp.text)
            soup = BeautifulSoup(resp.text, 'html.parser')
            return soup.find(tag)
    except Exception as e:
        print('Exception: %s' %(e))
        return None

def md_convert(projectName,step):

    url = 'https://raw.githubusercontent.com/raspberrypilearning/'+projectName+'/master/en/step_'+step+'.md'
    resp = requests.get(url)
    # mark = marko.convert(resp.text)
    # mark = resp.text
    # soup = BeautifulSoup(mark, 'html.parser')

    conText = resp.text
    # conText = cc.convert(conText)
    # conText = translator.translate(conText, src='en',dest='zh-tw').text
    iframeBlock = ""
    
    try:
        content = conText[:conText.index('<div')]+conText[conText.index('</div'):]
        content = content.replace("</div>","[[☃ iframe 1]]",1)
        content = content.replace("</div>","")
        iframeUrl = get_tag(url,'iframe')['src']
        # micro bit spacail 
        # iframeID = get_tag(url,'iframe')['src'].split("id=")[1]
        # iframeUrl = "https://ys-fang.github.io/msmc/player.html?id="+iframeID

        ifTemplete = junyiJSONgenerate.JSON_open('src\Templete\JSONiframe')
        iframeBlock = ifTemplete.replace("https://ys-fang.github.io/Linkit7697Learning-Resources/bubble/ROUTE/BUBBLEIDX.html",iframeUrl)
        iframeBlock = iframeBlock.replace("IFRAMEIDX",str(1))
    except Exception as e:
        content = conText
        print(e)

    imgIdx = 0
    while(content.find("![screenshot]",0)>0):
        imgIdx+=1
        content = content.replace("![screenshot]","[[☃ image "+str(imgIdx)+"]]",1)
    content = content.replace("(images/","(https://raw.githubusercontent.com/raspberrypilearning/"+projectName+"/master/en/images/")
    imgLink = re.findall(r'[(](https://raw.*?)[)]', content)
    content = re.sub(r'[(](https://raw.*?)[)]', "", content)
    while(imgIdx>0):
        templete = junyiJSONgenerate.JSON_open('src\Templete\JSONimage')
        string = templete.replace("IMGBLOCKINDEX",str(imgIdx))
        string = string.replace("https://ys-fang.github.io/Linkit7697Learning-Resources/img/ROUTE/IMGIDX.gif",imgLink[imgIdx-1])
        string = string.replace("IMAGEWIDTH",str(imgDownload.search_img_width(imgLink[imgIdx-1]).width))
        string = string.replace("IMAGEHEIGHT",str(imgDownload.search_img_width(imgLink[imgIdx-1]).height))
        imgIdx-=1
        iframeBlock += string
    iframeBlock = iframeBlock[:-1]
    
    while 1:
        if(content.find('<a')>=0):
            try:
                a_link = get_tag(url,'a')
                content = content[:content.index('<a')]+"["+a_link.text+"](\""+a_link["href"]+"\",\" \" \"_blank\")"+content[content.index('</a>')+4:]
            except Exception as e:
                break
        else:
            break
    content = content.replace("){:target=\"_blank\"}"," \"_blank\" \"title\")")
    content = content.replace("--- no-print ---","")
    content = content.replace("--- /no-print ---","")
    # content = translator.translate(content, src='en',dest='zh-tw').text
    # content = content.replace("# "," **")
    articleBlockIdx = 1
    articleBlockContent = ""
    while 1:
        tempCont = content
        if(tempCont.find('--- collapse ---')>0): 
            content = tempCont[:tempCont.index('--- collapse ---')]+"[[☃ article-block "+str(articleBlockIdx)+"]]"+tempCont[tempCont.index('--- /collapse ---')+17:]
            arTemplete = junyiJSONgenerate.JSON_open('src\Templete\JSONartblo')
            artTemp = (tempCont[tempCont.index('--- collapse ---')+17:tempCont.index('--- /collapse ---')]).replace('"','\\"')
            title = artTemp[artTemp.find("---")+3:artTemp.find("---",1)]
            artTemp = artTemp.replace("\n","\\n")
            title = title.replace("\n","")
            artTemp = artTemp.replace(title,"")
            articleBlock = arTemplete.replace("CONTENT",artTemp)
            articleBlock = articleBlock.replace("TITLE",title.replace("title:","📍"))
            articleBlock = articleBlock.replace("ARTICLEIDX",str(articleBlockIdx))
            articleBlockContent+=articleBlock
            articleBlockIdx+=1
        elif(tempCont.find('--- hints ---')>0):
            content = tempCont[:tempCont.index('--- hints ---')]+"[[☃ article-block "+str(articleBlockIdx)+"]]"+tempCont[tempCont.index('--- /hints ---')+17:]
            arTemplete = junyiJSONgenerate.JSON_open('src\Templete\JSONartblo')
            artTemp = (tempCont[tempCont.index('--- hints ---')+17:tempCont.index('--- /hints ---')]).replace('"','\\"')
            # title = artTemp[artTemp.find("---")+3:artTemp.find("---",1)]
            artTemp = artTemp.replace("\n","\\n")
            artTemp = artTemp.replace("--- hint ---","")
            artTemp = artTemp.replace("--- /hint ---","")
            # title = title.replace("\n","")
            # artTemp = artTemp.replace(title,"")
            articleBlock = arTemplete.replace("CONTENT",artTemp)
            articleBlock = articleBlock.replace("TITLE",r"💡 我需要一點提示")
            articleBlock = articleBlock.replace("#fee","#ffe7c9")
            articleBlock = articleBlock.replace("ARTICLEIDX",str(articleBlockIdx))
            articleBlockContent+=articleBlock
            articleBlockIdx+=1
        elif(tempCont.find('--- task ---')>0):
            content = tempCont[:tempCont.index('--- task ---')]+"[[☃ article-block "+str(articleBlockIdx)+"]]"+tempCont[tempCont.index('--- /task ---')+13:]
            arTemplete = junyiJSONgenerate.JSON_open('src\Templete\JSONartblo')
            artTemp = (tempCont[tempCont.index('--- task ---')+13:tempCont.index('--- /task ---')]).replace('"','\\"')
            artTemp = artTemp.replace("\n","\\n")
            artTemp = artTemp.replace("--- hint ---","")
            artTemp = artTemp.replace("--- /hint ---","")
            articleBlock = arTemplete.replace("CONTENT",artTemp)
            articleBlock = articleBlock.replace("TITLE","")
            articleBlock = articleBlock.replace("#fee","#eafaec")
            articleBlock = articleBlock.replace("ARTICLEIDX",str(articleBlockIdx))
            articleBlock = articleBlock.replace("expandable\": true","expandable\": false")
            articleBlockContent+=articleBlock
            articleBlockIdx+=1
        else:
            break
    

    # print(get_tag_text(url,'h2'))
    # print(get_tag(url,'a'))
    # print(get_tag_text(url,'li'))

    templete = junyiJSONgenerate.JSON_open('src\Templete\JSONempty')
    content = content.replace("\n","\\n")
    content = content.replace('"','\\"')
    output = templete.replace("CONTENT",content)
    output = output.replace("WIDGETS",iframeBlock+articleBlockContent[:-1])
    print(projectName+str(stepIdx)+"finish!"+stepIdx*"🧨🧨")
    output = output.replace("}\"article-block","},\"article-block")
    output = output.replace("	","")
    RC = output.replace("/master",'')
    RC = RC.replace("https://raw.githubusercontent.com/raspberrypilearning","https://raw.githubusercontent.com/ys-fang/Code-Club-Learning-Resources/master")
    RC = RC.replace("/tree",'')
    RC = RC.replace("/blob",'')
    RC = RC.replace("/en/","/zh-CN/")
    output = RC.replace("https://github.com/raspberrypilearning","https://github.com/ys-fang/Code-Club-Learning-Resources/blob/master")
    if not os.path.isdir("output/raspberrypilearning/"+projectName):
        os.mkdir("output/raspberrypilearning/"+projectName)
    junyiJSONgenerate.JSON_write(output,"output/raspberrypilearning/"+projectName+"/"+projectName+"-"+step)

f = open("D:/workspace/HtmlParseBot/HtmlParse/output/raspberrypilearning/pathList.txt", "r",encoding = 'utf8')
for x in f:
    print(x)
    projectName = x.replace("\n",'')
    # os.mkdir(projectName)
    stepIdx = 1
    while 1:
        
        # projectName = 'happy-birthday'
        step = stepIdx
        url = 'https://raw.githubusercontent.com/raspberrypilearning/'+projectName+'/master/en/step_'+str(step)+'.md'
        resp = requests.get(url)
        # print(resp.text)
        if resp.status_code == 200:
            md_convert(projectName,str(stepIdx))
            # exportCSV.add_csv(projectName,step)
            stepIdx+=1
        else:
            break
        