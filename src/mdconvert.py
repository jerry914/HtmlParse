import marko
import requests
from bs4 import BeautifulSoup


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

url = 'https://raw.githubusercontent.com/raspberrypilearning/interactive-badge/master/en/step_1.md'
resp = requests.get(url)
mark = marko.convert(resp.text)
soup = BeautifulSoup(mark, 'html.parser')

# print(resp.text)
print(get_tag_text(url,'h2'))
print(get_tag(url,'iframe'))
print(get_tag(url,'collapse'))
print(get_tag_text(url,'li'))