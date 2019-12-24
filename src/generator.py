import junyiJSONgenerate
import json
import sqlite3


def titleSplit(section,subtitle):
    title = section.split("|")
    mdtitle = title[1]+"\n"+title[2].replace(subtitle,'')
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
        string+="[[☃ "+blockType+" "+str(n+1)+"]]\n\n"
    return string

def artBlk_wigit_generate(num,Type,route,idx):
    string = ''
    if(Type == 'm'):
        for n in range(num):
            string+='''"image '''+str(n+1)+'''": {
                            "graded": true,
                            "id": "image '''+str(n+1)+'''",
                            "options": {
                                "aspectRatio": 0.3352941176470588,
                                "backgroundImage": {
                                    "url": "https://jerry914.github.io/Linkit7697Learning-Resources/img/'''+route+'''+/'''+str(idx)+'''.gif",
                                    "width": 435
                                },
                                "box": [],
                                "labels": [],
                                "maxImageSize": 435,
                                "range": [
                                    [
                                        0,
                                        10
                                    ],
                                    [
                                        0,
                                        10
                                    ]
                                ],
                                "useBoxSize": false
                            },
                            "type": "image",
                            "version": {
                                "major": 0,
                                "minor": 0
                            }
                        },'''
        return string[:-1]
    else:
        for n in range(num):
            string+='''"iframe '''+str(n+1)+'''": {
                "type": "iframe",
                "graded": true,
                "options": {
                    "url": "https://jerry914.github.io/Linkit7697Learning-Resources/bubble/'''+route+'/'+str(idx)+'''.html",
                    "settings": [
                        {
                            "name": "",
                            "value": ""
                        }
                    ],
                    "width": 560,
                    "height": 320
                },
                "version": {
                    "major": 0,
                    "minor": 0
                }
            },'''
        return string

def cont_wiget_generate(sectionText,sectionImgCount,sectionBubbleCount,route):
    templete = junyiJSONgenerate.JSON_openTemplete()
    footerContent = templete["question"]["widgets"]["article-block 1"]["options"]["widgets"]
    # bubbleIdx = 1
    # imgIdx = 1

    # temp = json.dumps({"article-block 1": footerContent})
    # temp=json.dumps({"article-block 1": {"age":"fff"}})
    print(footerContent)
    # for a in range(len(sectionText)-2):
    #     articleBlock = junyiJSONgenerate.JSON_open('src\Templete\JSONartblo')
    #     json = json.dumps({'article-block'+a: articleBlock['article-block 1']})
    #     bubbleIdx+=len(sectionBubbleCount)
    #     imgIdx+=len(sectionImgCount)

    widget = footerContent
    return widget
                        