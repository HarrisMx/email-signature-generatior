from bs4 import BeautifulSoup as bs
import csv
import re

with open('csv/emailsignature_v1.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    for row in reader:
        name = row[0]
        job_title = row[1]
        email = row[2]
        cellphone_number = row[3]

        if cellphone_number == "":
            continue

        page = open("html/signature_template.html") #Your html template should be in a folder named 'html'
        html = bs(page.read(),'html.parser')

        _name = html.find("td", {"class": "name"})
        _job_title = html.find("td", {"class": "job_title"})
        _number = html.find("td", {"class": "contact_number"})
        title = html.find('title')
        
        _name.string.replace_with(str(name))
        _number.string.replace_with(str(cellphone_number))
        _job_title.string.replace_with(str(job_title))
        title.string.replace_with(str(_name.string))

        file = open('output/'+str(_name.string)+'.html', 'w') #Your output files will be saved in a folder named 'output'

        file.write(str(html))

        file.close()
        
print("Done!!!")