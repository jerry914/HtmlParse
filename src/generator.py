import junyiJSONgenerate
import json
import sqlite3


def titleSplit(section,subtitle):
    title = section.split("|")
    mdtitle = title[1]+"\\n"+title[2].replace(subtitle,'')
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
    artTemplete = junyiJSONgenerate.JSON_open('src\Templete\JSONartblo')
    if(Type == 'm'):
        for n in range(num):
            templete = junyiJSONgenerate.JSON_open('src\Templete\JSONimage')
            string = templete.replace("IMGBLOCKINDEX",str(n+1))
            string = string.replace("ROUTE",route)
            string = string.replace("IMGIDX",str(idx))
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
    for a in range(len(sectionText)-2):
        articleBlock = templete.replace("ARTICLEIDX",str(a))
        articleBlock = articleBlock.replace("IFRAMEBLOCK",artBlk_wigit_generate(a,'f',route,bubbleIdx))
        articleBlock = articleBlock.replace("IMGBLOCK",artBlk_wigit_generate(a,'m',route,imgIdx))
        bubbleIdx+=len(sectionBubbleCount)
        imgIdx+=len(sectionImgCount)
        result+=articleBlock

    return result
                        