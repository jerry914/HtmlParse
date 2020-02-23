import csv
import re


with open('junyi_question0.csv', newline='',encoding = 'utf8') as csvfile2:
    rows = csv.reader(csvfile2)
    for row in rows:
        RC = row[6]
        
        if(RC.find("程式")>=0):
            RC = RC.replace("程式","代")
        # if(RC.find("--- challenge ---")>=0):
        #     RC = RC.replace("#fff","#fee")
        #     RC = RC.replace("## Challenge","# ⚔️ Challenge")
        #     RC = RC.replace("--- challenge ---","")
        #     RC = RC.replace("--- /challenge ---","")
        
        # with open("temp/"+row[4]+"-"+row[0]+".txt", 'w',encoding = 'utf8') as f: 
        #     f.write(RC)
        # f.close()

        # RC = RC.replace('\n','')

            with open('junyi.csv','a+', newline='',encoding = 'utf8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([row[0],row[1],row[2],row[3],row[4],row[5],RC,row[7],row[8]])
            csvfile.close()
    csvfile2.close()
