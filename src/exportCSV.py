import csv

def add_csv(projectName,step):
    try:
        route = projectName+'/'+projectName+'-'+str(step)
        filepath = "D:/workspace/HtmlParseBot/HtmlParse/output/raspberrypilearning/"+route
        f = open(filepath+".txt", "r",encoding = 'utf8')
        enCode=''
        for line in f.readlines():
            enCode+=line.replace('\n','')
            # print(enCode)
        
        with open('D:/workspace/HtmlParseBot/HtmlParse/output/output.csv', 'a+', newline='',encoding = 'utf8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['0','False','電腦科學','Code Club - Raspberry Pi Foundation',projectName,'1',enCode,'',''])
        csvfile.close()
    except Exception as e:
        print(e)


# pathIdx = -1
# idx = 0
# f = open("D:/workspace/HtmlParseBot/Linkit7697Learning Resources/pathList.txt", "r",encoding = 'utf8')
# for x in f:
#     print(x)
#     nowpath = x
#     if(nowpath.find("/")<0):
#         idxpath = nowpath
#         pathIdx+=1
#     try:
#         route = x.replace("\n",'')
#         filepath = "D:/workspace/HtmlParseBot/HtmlParse/output/"+route
#         f = open(filepath+".txt", "r",encoding = 'utf8')
#         enCode=''
#         for line in f.readlines():
#             enCode+=line.replace('\n','')
#             # print(enCode)
        
#         with open('D:/workspace/HtmlParseBot/HtmlParse/output/output.csv', 'a+', newline='',encoding = 'utf8') as csvfile:
#             writer = csv.writer(csvfile)
#             writer.writerow([idx,'False','電腦科學','',"linkit\ncs-linkit-basic-1-"+str(pathIdx),'1',enCode,'',''])
#             idx+=1
#         csvfile.close()
#     except Exception as e:
#         print(e)