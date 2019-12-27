import junyiJSONgenerate
import json
import sqlite3
import imgDownload
fileRootPath = str('D:/workspace/HtmlParseBot/Linkit7697Learning Resources/')

def titleSplit(section,subtitle):
    title = section.split("|")
    mdtitle = title[1]+" "+title[2].replace(subtitle,'')
    return mdtitle

def artBlk_generate(num,Type):
    string = ''
    blockType = ''
    if(Type == 'a'):
        blockType = "article-block"
    elif(Type == 'm'):
        blockType = "image"
    else:
        blockType = "iframe"
    for n in range(num):
        string+="[[☃ "+blockType+" "+str(n+1)+"]]\\n\\n"
    return string

def artBlk_wigit_generate(num,Type,route,idx):
    resuleString = ''
    if(Type == 'm'):
        for n in range(num):
            templete = junyiJSONgenerate.JSON_open('src\Templete\JSONimage')
            string = templete.replace("IMGBLOCKINDEX",str(n+1))
            string = string.replace("ROUTE",route)
            string = string.replace("IMGIDX",str(idx))
            imgfilePath = fileRootPath+'img/'+route+'/'
            string = string.replace("IMAGEWIDTH",str(imgDownload.search_img_width(imgfilePath+str(idx)+".gif").width))
            string = string.replace("IMAGEHEIGHT",str(imgDownload.search_img_width(imgfilePath+str(idx)+".gif").height))
            resuleString+=string
        return resuleString[:-1]
    else:
        for n in range(num):
            templete = junyiJSONgenerate.JSON_open('src\Templete\JSONiframe')
            string = templete.replace("IFRAMEIDX",str(n+1))
            string = string.replace("ROUTE",route)
            string = string.replace("BUBBLEIDX",str(idx))
            resuleString+=string
        return resuleString

def cont_wiget_generate(sectionText,sectionImgCount,sectionBubbleCount,route):
    templete = junyiJSONgenerate.JSON_open('src\Templete\JSONartblo')
    bubbleIdx = 1
    imgIdx = 1
    result =  ''
    for a in range(1,len(sectionText)-2):
        articleBlock = ''
        articleBlock = templete.replace("ARTICLEIDX",str(a+1))
        articleBlock = articleBlock.replace("ARTICLETEXT",sectionText[a+1])
        articleBlock = articleBlock.replace("IFRAMEBLOCK",artBlk_wigit_generate(sectionBubbleCount[a+1],'f',route,bubbleIdx))
        articleBlock = articleBlock.replace("IMGBLOCK",artBlk_wigit_generate(sectionImgCount[a+1],'m',route,imgIdx))
        if(articleBlock.find('width": 70')>0 or articleBlock.find('width": 170')>0):
            articleBlock = articleBlock.replace("#fff",'')
            articleBlock = articleBlock.replace("ARTICLESTYLE",'# ')
        else:
            articleBlock = articleBlock.replace("ARTICLESTYLE",'')
        bubbleIdx+=sectionBubbleCount[a]
        imgIdx+=sectionImgCount[a+1]
        result+=articleBlock

    return result[:-1]
                        