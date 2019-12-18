import requests
from bs4 import BeautifulSoup
import csv
url = input("Enter URL: ")
fileName = input("Enter File Name: ")

res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

count=0
intros = []
thisSection = []
learnTemp = ''
willLearn = []
footer = ''


for drink in soup.select('{}'.format('h3')):
    if drink.get_text() !='':
        print(drink.get_text())
        if count<3:
            intros.append(drink.get_text())
        elif count<8 and count>=3:
            if(drink.get_text().find('設備')):
                drink.get_text().replace('設備','硬體')
            thisSection.append(drink.get_text().replace('‣',''))
        elif count ==8:
            print("noGet")
        else:
            temp = drink.get_text().split(" ")
            learnTemp = ''
            for tc in temp:
                if tc != '':
                    learnTemp+='['+tc+'] '
            willLearn.append(learnTemp)
        count+=1

for drink in soup.select('{}'.format('section')):
    footer = drink.get_text()
footer = footer.replace('+ ShareFacebookLINEGoogleClassroom','')
footer = footer.replace('+ About','')
footerList=list(footer)
footEnterPos=footer.index('Scratch 是一種程式語言')
footerList.insert(footEnterPos,r'\n\n')
footer="".join(footerList)

className = input("主題名稱?")
for i in intros:
    print(i)
for t in thisSection:
    print(t)
for w in willLearn:
    print(w)



with open(fileName+".txt", 'w+',encoding = 'utf8') as f: 
    f.write(r'''{
    "question": {
        "content": "[[☃ iframe 1]]\n[[☃ article-block 1]]\n[[☃ explanation 1]]",
        "images": {},
        "widgets": {
            "iframe 1": {
                "type": "iframe",
                "graded": true,
                "options": {
                    "height": 400,
                    "settings": [
                        {
                            "name": "",
                            "value": ""
                        }
                    ],
                    "url": "",
                    "width": 560
                },
                "version": {
                    "major": 0,
                    "minor": 0
                }
            },
            "article-block 1": {
                "type": "article-block",
                "graded": false,
                "options": {
                    "articleBlock": "$\\huge{%s}$\n\n$\\\\$\n\n%s\n\n%s\n\n%s\n\n$\\\\$ \n\n[[☃ article-block 1]]\n\n$\\\\$ \n\n[[☃ article-block 2]]\n\n$\\\\$ \n\n[[☃ article-block 3]]\n\n$\\\\$\n\n$\\Large{現在，讓我們一起開始吧！}$　 \n$\n\\require{enclose}\n\\enclose{box}[mathcolor=\"#4cae4c\",mathbackground=\"#\"]{\\large\\color{}{ 　下一步　}}\n\\\\\n$ \n",
                    "background": "",
                    "blockTitle": "",
                    "widgets": {
                        "article-block 1": {
                            "graded": false,
                            "id": "article-block 1",
                            "options": {
                                "articleBlock": "○ %s\n\n○ %s\n\n○ %s\n\n○ %s\n\n○ %s\n\n○ 軟體需求：使用 Scratch 3.0 [線上版（推薦）](https://scratch.mit.edu/ \"online\" \"_blank\") 或 [離線版](https://scratch.mit.edu/download \"offline\" \"_blank\")。\n\n[[☃ article-block 1]]",
                                "background": "#def",
                                "blockTitle": "ℹ️ 這個主題活動",
                                "widgets": {
                                    "article-block 1": {
                                        "graded": false,
                                        "id": "article-block 1",
                                        "options": {
                                            "articleBlock": "📣 小建議 \n  \n如果習慣使用 Scratch 2.0，可以前往[均一 Scratch2.0 學習專區](https://www.junyiacademy.org/course/scratch2 \"scratch2\" \"_blank\")。",
                                            "background": "aliceblue",
                                            "blockTitle": "",
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
                        },
                        "article-block 2": {
                            "graded": false,
                            "id": "article-block 2",
                            "options": {
                                "articleBlock": "[[☃ inline-scratch 1]] \n",
                                "background": "#e0f0f5",
                                "blockTitle": "ℹ️ 你會學到的事",
                                "widgets": {
                                    "article-block 1": {
                                        "graded": false,
                                        "id": "article-block 1",
                                        "options": {
                                            "articleBlock": "[[☃ inline-scratch 1]]\n\n[[☃ inline-scratch 2]]",
                                            "background": "#fff",
                                            "blockTitle": "",
                                            "widgets": {}
                                        },
                                        "type": "article-block",
                                        "version": {
                                            "major": 0,
                                            "minor": 0
                                        }
                                    },
                                    "inline-scratch 1": {
                                        "graded": true,
                                        "id": "inline-scratch 1",
                                        "options": {
                                            "scratchText": "► 核心概念：%s :: #71DAC1\n\n► 相關概念：%s :: #71DAC1\n",
                                            "scratchVersion": "scratch3"
                                        },
                                        "type": "inline-scratch",
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
                        "article-block 3": {
                            "graded": false,
                            "id": "article-block 3",
                            "options": {
                                "articleBlock": "○ 老師備課教學，可參考：[[ 45分鐘教學指引 ]](http://example.com/ \"educatorGuide\" \"_blank\")。\n\n○ 課堂活動的學習單：[[ 偵探記錄簿 ]](http://example.com/ \"worksheet\" \"_blank\")。\n\n○ 下載課程的[[ 範例專案 ]](http://example.com/ \"Title\" \"_blank\")，在Scratch離線編輯器使用。",
                                "background": "#e0f0f5",
                                "blockTitle": "ℹ️ 教師的備課素材",
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
                "version": {
                    "major": 0,
                    "minor": 0
                }
            },
            "explanation 1": {
                "type": "explanation",
                "graded": false,
                "options": {
                    "explanation": "%s\n\n[[☃ image 1]]",
                    "hidePrompt": "− 隱藏說明",
                    "showPrompt": "+ 關於課程 ABOUT",
                    "widgets": {
                        "image 1": {
                            "graded": true,
                            "id": "image 1",
                            "options": {
                                "aspectRatio": 0.255663430420712,
                                "backgroundImage": {
                                    "height": 19,
                                    "url": "https://junyiexerciseimgtest.s3.amazonaws.com/scratch3-01/3127/6",
                                    "width": 75
                                },
                                "box": [
                                    75,
                                    19
                                ],
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
                                "useBoxSize": true
                            },
                            "type": "image",
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
}'''%(className,intros[0],intros[1],intros[2],thisSection[0],thisSection[1],thisSection[2],thisSection[3],thisSection[4],willLearn[0],willLearn[1],footer))

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
    writer.writerow(['3148','False','電腦科學','','scratch3-05','1',enCode,'',''])
csvfile.close()

f.close

