#藉由首頁取得所有文章的URL
import requests
from bs4 import BeautifulSoup
import json
import marko

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


# test = open("spider/img/test.txt","w",encoding='UTF-8')

url = 'https://sites.google.com/junyiacademy.org/linkit7697/getstart/%E5%9F%BA%E7%A4%8E%E9%9B%BB%E5%AD%B8%E8%A7%80%E5%BF%B5'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

sectionBlock = soup.find_all('section')
imgBlock = soup.find_all('small')
for d in sectionBlock:
    # print(d.get_text())
    try: 
        img = d.find_all('img')
        imgText = d.find_all('small')
        for i in range(len(img)):
            print(imgText[i].text)
            print(img[i]["src"])
            pic=requests.get(img[i]["src"])
            img2 = pic.content
            pic_out = open("spider/img/"+str(imgText[i].text)+".png",'wb')
            pic_out.write(img2)
            pic_out.close()
    except Exception as e:
        print(e)

# imgLink = soup.find_all('img')
# q=0
# print(imgLink)
# for img in imgLink:
#     q+=1
#     print(img["src"])
#     pic=requests.get(img["src"])
#     img2 = pic.content
#     pic_out = open("spider/img/"+str(q)+".png",'wb')
#     pic_out.write(img2)
#     pic_out.close()


# test.close()
print("爬蟲結束")