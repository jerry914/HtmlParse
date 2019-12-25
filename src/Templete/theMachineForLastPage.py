import requests
import csv
from bs4 import BeautifulSoup

rootUrl = input("URl")
index = '06'

for stepIndex in range(1,2):
    tag = 'h1'
    titleNum = 0
    titles=[]
    sections=[[]]
    count = 0
    sectionColor="#FFF"
    url = rootUrl
    fileName = input("fileName")

    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    for drink in soup.select('{}'.format(tag)):
        #print(drink.get_text())
        titles.append(drink.get_text())
        sections.append([])
        titleNum+=1
        #print("---------------------------*************-")

    for drink in soup.select('{}'.format('h2')):
        #print(drink.get_text())
        titles.append(drink.get_text())
        sections.append([])
        titleNum+=1
        #print("---------------------------*************-")

    
    #find the class name
    name_box = soup.find('h1')
    name = name_box.text.strip()
    print("name: "+name)

    #how many secondary article block
    titleNum-=1
    print("titles: ")
    print(titleNum)


    for drink in soup.select('{}'.format('section')):
        if (drink.get_text() != ''):
            readStr = drink.get_text()
            if(count <= titleNum):
                strPos = readStr.find(titles[count])
                if(strPos==0):
                    count+=1
                    if readStr != '玩一玩，想一想':
                        sections[count-1].append(readStr[len(titles[count-1]):])  
                else:
                    sections[count-1].append(readStr)
            else:
                sections[count-1].append(readStr)
        
        
        #sections.append(drink.get_text())
        #print(count,drink.get_text())
    count=0
    for index in sections:
        if(len(titles) <= count):
            print("")
        else:
            print(titles[count])
        
        for section in index:
            print(section)
        count+=1




    with open(fileName+".txt", 'w+',encoding = 'utf8') as f: 
        f.write(r'''{
        "question": {
            "content": "[[☃ article-block 2]]\n",
            "images": {},
            "widgets": {
                "article-block 2": {
                    "type": "article-block",
                    "graded": false,
                    "options": {
                        "articleBlock": "$\\huge{📦 ''')
        f.write(name+r"}$\n\n$\\\\$\n\n")
        for section in sections[0]:
            f.write(section)
        f.write(r"\n\n$\\\\$ \n\n")
        for i in range(titleNum-1):
            f.write('[[☃ article-block '+str(i+1)+r"]]\n\n")

        f.write(r'''\n\n[[☃ article-block ''')
        f.write(str(titleNum)+r''']]\n",
                        "background": "#f5f5dc",
                        "blockTitle": "",
                        "widgets": {''')
        for title in range(1,titleNum+1):
            f.write(r'''"article-block %d": {
                                "graded": false,
                                "id": "article-block %d",
                                "options": {
                                    "articleBlock": "\n\n'''%(title, title))
            if(title==1):
                startNum = 0
            else:
                startNum = 1
            for section in range(startNum,len(sections[title])):
                f.write(r'''\n\n[[☃ article-block %d]]'''%section)
            if(titles[title]=='玩一玩，想一想'):
                f.write(r'''",
                                    "background": "#e0f0f5",
                                    "blockTitle":"💬  %s",
                                    "widgets": {'''%titles[title])
                sectionColor = ""
            else:
                
                f.write(r'''",
                                    "background": "#ffffe9",
                                    "blockTitle":"🔖  %s",
                                    "widgets": {'''%titles[title])
                sectionColor = ""
                
            for section in range(startNum,len(sections[title])):
                f.write(r'''"article-block %d": {
                                            "type": "article-block",
                                            "graded": false,
                                            "id": "article-block %d",
                                            "options": {
                                                "articleBlock": " %s \n\n[[☃ image 1]]",
                                                "background": "%s",
                                                "blockTitle": "",
                                                "widgets": {
                                                    "image 1": {
                                                        "graded": true,
                                                        "options": {
                                                        "type": "image",
                                                            "useBoxSize": false,
                                                            "backgroundImage": {
                                                                "url": ""
                                                            },
                                                            "labels": [],
                                                            "maxImageSize": 640
                                                        },
                                                        "version": {
                                                            "major": 0,
                                                            "minor": 0
                                                        }
                                                    }
                                                }
                                            },
                                            "version": {
                                                "major": 0,
                                                "minor": 0
                                            }
                                        }'''%(section,section,sections[title][section],sectionColor))
                if(section!=len(sections[title])-1):
                    f.write(',')
            f.write(r''' }},"type": "article-block",
                                "version": {
                                    "major": 0,
                                    "minor": 0
                                }
                            }''')
            if(title!=titleNum):
                f.write(',')
                
        f.write(r'''
                        }
                    },
                    "version": {
                        "major": 0,
                        "minor": 0
                    }
                }
            }
        },
        "answerArea": {
            "type": "multiple",
            "options": {},
            "calculator": false
        },
        "itemDataVersion": {
            "major": 0,
            "minor": 1
        },
        "hints": []
    }''')

            
    # Close opend file
    f.close()

    f = open(fileName+".txt", "r",encoding = 'utf8')
    enCode=''
    for line in f.readlines():
        enCode+=line.replace('\n','')
    print(enCode)
    with open('output1.csv', 'a+', newline='',encoding = 'utf8') as csvfile:
        # 建立 CSV 檔寫入器
        writer = csv.writer(csvfile)
        # 寫入一列資料
        writer.writerow([fileName+index,'False','電腦科學','','scratch3-'+index,'1',enCode,'',''])
    csvfile.close()

    f.close

