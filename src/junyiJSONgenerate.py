import json
from pprint import pprint
import generator

def JSON_openTemplete():
    with open("src/Templete/JSONtemplete.json", 'r',encoding = 'utf8') as tf: 
        templete = json.load(tf)
        tf.close()
        return templete

def JSON_open(fileName):
    with open(fileName+".json", 'r',encoding = 'utf8') as f: 
        data = json.load(f)
        pprint(data)
        f.close()
        return data

def JSON_generate(fileName,sectionText,subtitle,sectionImgCount,sectionBubbleCount,route):
    templete = JSON_openTemplete()
    templete["question"]["content"] = "# "+generator.titleSplit(sectionText[0],subtitle)+"\n\n[[☃ article-block 1]]"
    templete["question"]["widgets"]["article-block 1"]["options"]["articleBlock"] = "# "+subtitle+"\n"+sectionText[1]+"\n"+generator.artBlk_generate(len(sectionText)-2,'a')+"[[☃ explanation 1]]\n\n[[☃ explanation 2]]\n\n[[☃ image 1]]\n\n[[☃ image 2]]"
    # templete["question"]["widgets"]["article-block 1"]["options"]["widgets"] = generator.cont_wiget_generate(sectionText,sectionImgCount,sectionBubbleCount,route)
    
    with open(fileName+".txt", 'w',encoding = 'utf8') as f:
        f.write(str(templete).replace("'",'"'))
        f.close()


# JSON_open('output/getstart/基礎電學觀念')
