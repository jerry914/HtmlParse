import csv
import re

newRow = []
tempRow = []
with open('junyi_question0.csv', newline='',encoding = 'utf8') as csvfile:
  rows = csv.reader(csvfile)
  for row in rows:
    tempRow.append(row)
for row in tempRow:
    newRow.append(str(row).replace('''maxImageSize": 435''','''maxImageSize": 640'''))
with open('junyi_question1.csv','a+', newline='',encoding = 'utf8') as csvfile:
    writer = csv.writer(csvfile)
    for row in newRow:
        print(row)
        writer.writerow([row])
csvfile.close()