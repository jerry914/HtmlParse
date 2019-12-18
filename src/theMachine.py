import requests
import csv
from bs4 import BeautifulSoup

rootUrl = 'https://sites.google.com/junyiacademy.org/cs101-music/step'
stepNum = 5

for stepIndex in range(1,stepNum+1):
    tag = 'h1'
    titleNum = 0
    titles=[]
    sections=[[]]
    count = 0
    sectionColor="#FFF"
    url = rootUrl+str(stepIndex)
    fileName = '11-'+str(stepIndex)

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
            if (drink.get_text().find('+ About')==-1 and drink.get_text().find('- - -跟著指引，一起進行- - -')==-1):
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
            "content": "[[☃ article-block 1]]\n",
            "images": {},
            "widgets": {
                "article-block 1": {
                    "type": "article-block",
                    "graded": false,
                    "options": {
                        "articleBlock": "$\\huge{''')
        f.write(name+r"}$\n\n$\\\\$\n\n")
        for section in sections[0]:
            f.write(section)
        f.write(r"\n\n$\\\\$ \n\n")
        if stepIndex == 2:
            f.write(r'''[[☃ article-block 16]]\n\n''')
        for i in range(titleNum-1):
            f.write('[[☃ article-block '+str(i+1)+r"]]\n\n")

        f.write(r'''$\\\\$\n\n\n$\n\\require{enclose}\n\\enclose{box}[mathcolor=\"#4cae4c\",mathbackground=\"#\"]{\\large\\color{}{ 　下一步 ❯　}}\n\\\\\n$ \n\n$\\Large{　}$\n\n$\\\\$ \n\n[[☃ article-block ''')
        f.write(str(titleNum)+r''']]\n",
                        "background": "",
                        "blockTitle": "",
                        "widgets": {''')
        if stepIndex == 2:
            f.write(r''' "article-block 16": {
                            "graded": false,
                            "id": "article-block 16",
                            "options": {
                                "articleBlock": "$\\\\$ \n\n你可以選擇使用 Scratch **網路社群版** 或 **離線桌面版**，來製作專案作品。\n\n[[☃ article-block 1]]\n\n[[☃ article-block 2]]",
                                "background": "#def",
                                "blockTitle": "🔖 開啟\b/登入 SCRATCH",
                                "widgets": {
                                    "article-block 1": {
                                        "graded": false,
                                        "id": "article-block 1",
                                        "options": {
                                            "articleBlock": "\n\n前往 [ Scratch 首頁  ](https://scratch.mit.edu \"online\" \"_blank\")，並且註冊/登入 Scratch 帳號，就可以儲存專案、分享作品給好朋友哦！ \n\n[ 📔如何註冊Scratch (pdf) ](https://drive.google.com/open?id=1MeGhvjizyrmr-kXZyzwv-ZQjrF53fbrG \"register_howto\" \"_blank\")\n\n$\\\\$\n\n✅ Scratch 首頁像是這樣子：\n\n[[☃ image 1]]",
                                            "background": "aliceblue",
                                            "blockTitle": "🌏 網路社群版",
                                            "widgets": {
                                                "image 1": {
                                                    "graded": true,
                                                    "id": "image 1",
                                                    "options": {
                                                        "aspectRatio": 0.5447916666666667,
                                                        "backgroundImage": {
                                                            "height": 1569,
                                                            "url": "https://drive.google.com/uc?export=view&id=1mzEaejbDaqDaPNOuqkU09wyNmPpWSA8a",
                                                            "width": 2880
                                                        },
                                                        "box": [
                                                            640,
                                                            349
                                                        ],
                                                        "labels": [],
                                                        "maxImageSize": 640,
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
                                                }
                                            }
                                        },
                                        "type": "article-block",
                                        "version": {
                                            "major": 0,
                                            "minor": 0
                                        }
                                    },
                                    "article-block 2": {
                                        "graded": false,
                                        "id": "article-block 2",
                                        "options": {
                                            "articleBlock": "\n\n前往[ Scratch下載頁面 ](https://scratch.mit.edu/download \"offline\" \"_blank\")，下載並安裝 Scratch 3.0。",
                                            "background": "aliceblue",
                                            "blockTitle": "🖥 離線桌面版",
                                            "widgets": {}
                                        },
                                        "type": "article-block",
                                        "version": {
                                            "major": 0,
                                            "minor": 0
                                        }
                                    }
                                }
                            },
                            "type": "article-block",
                            "version": {
                                "major": 0,
                                "minor": 0
                            }
                        },''')
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
                if(title!=titleNum):
                    f.write(r'''",
                                        "background": "#def",
                                        "blockTitle":"🔖  %s",
                                        "widgets": {'''%titles[title])
                    sectionColor = "aliceblue"
                else:
                    f.write(r'''",
                                                    "background": "#f5f5dc",
                                                    "blockTitle": "📍TIPS:  %s",
                                                    "widgets": {''' % titles[title])
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
    with open('output.csv', 'a+', newline='',encoding = 'utf8') as csvfile:
        # 建立 CSV 檔寫入器
        writer = csv.writer(csvfile)
        # 寫入一列資料
        writer.writerow(['11','False','電腦科學','','scratch3-11','1',enCode,'',''])
    csvfile.close()

    f.close

