import marko
import requests
from bs4 import BeautifulSoup
import junyiJSONgenerate


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
            mark = marko.convert(resp.text)
            soup = BeautifulSoup(mark, 'html.parser')
            return soup.find(tag)
    except Exception as e:
        print('Exception: %s' %(e))
        return None


url = 'https://raw.githubusercontent.com/raspberrypilearning/interactive-badge/master/en/step_2.md'
resp = requests.get(url)
mark = marko.convert(resp.text)
soup = BeautifulSoup(mark, 'html.parser')

# print(resp.text)
conText = resp.text
iframeBlock = ""
try:
    content = conText[:conText.index('<div')]+conText[conText.index('</div')+6:]
    content = content.replace("</div>","[[☃ iframe 1]]")
    ifTemplete = junyiJSONgenerate.JSON_open('src\Templete\JSONiframe')
    iframeBlock = ifTemplete.replace("https://ys-fang.github.io/Linkit7697Learning-Resources/bubble/ROUTE/BUBBLEIDX.html",get_tag(url,'iframe')['src'])
    iframeBlock = iframeBlock.replace("IFRAMEIDX",str(1))
except Exception as e:
    content = conText
    print(e)
content = content.replace("(images/","(https://raw.githubusercontent.com/jerry914/interactive-badge/master/en/images/")
while 1:
    if(content.find('<a')>=0):
        a_link = get_tag(url,'a')
        content = content[:content.index('<a')]+"["+a_link.text+"](\""+a_link["href"]+"\",\" \" \"_blank\")"+content[content.index('</a>')+4:]
    else:
        break

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
print(output)

junyiJSONgenerate.JSON_write(output,"interactive-badge-2")