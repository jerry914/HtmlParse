import requests
from bs4 import BeautifulSoup
import os
from PIL import Image

def download_single_img(url,filePath):
    pic=requests.get(url)
    try:
        path = os.path.join(os.getcwd(),filePath+".gif")
    except Exception as e:
        print(e)
    img2 = pic.content
    pic_out = open(path,'wb')
    pic_out.write(img2)
    pic_out.close()


# https://jerry914.github.io/Linkit7697Learning-Resources/img/DIR/NAME.gif


print("爬蟲結束")