import requests_html
import csv
from requests_html import HTMLSession,HTMLResponse
from bs4 import BeautifulSoup

csv_file = open('ALL_FUNCTIONS(PYTHON).csv','w')
csv_writer = csv.writer(csv_file, lineterminator='\n')
csv_writer.writerow(['FUNCTION NAME', 'DESCRIPTION'])

session = HTMLSession()
link_part_1 = 'https://docs.python.org/3/library/'

links_li = []
function_name_li = []
discription_li = []

response1 = session.get(link_part_1).html
source1 = response1.html
for_link = BeautifulSoup(source1, 'lxml')

blocks1 = for_link.find_all('li', class_='toctree-l1')
blocks2 = for_link.find_all('li', class_='toctree-l2')
for block in blocks1:
    b1 = block.find_all('a', class_ = 'reference internal')[0]
    b1 = b1.attrs['href']
    links_li.append(link_part_1+b1)

for blocks in blocks2:
    b2 = blocks.find_all('a', class_ = 'reference internal')[0]
    b2 = b2.attrs['href']
    links_li.append(link_part_1+b2)

for link in links_li:
    response2 = session.get(link).html
    source2 = response2.html
    soup = BeautifulSoup(source2, 'lxml')
    boxes = soup.find_all('dl', class_ = 'function' )
    boxess = soup.find_all('dl', class_ = 'method')

    for box in boxes:
        name = box.find('dt')
        print(name.text[:-1:].strip())
        function_name_li.append(name.text[:-1:].strip())

        des = box.find('dd')
        print(des.text.strip())
        discription_li.append(des.text.strip())

        try:
            csv_writer.writerow([name.text[:-1:].strip(), des.text.strip()])
        except Exception as ex:
            print(ex)

        # csv_writer.writerow([name.text[:-1:].strip(), des.text.strip()])

        # if(name.text[:-1:].strip() and des.text.strip() != None):
        #     csv_writer.writerow([name.text[:-1:].strip(), des.text.strip()])
        # elif(des.text.strip() == None):
        #     csv_writer.writerow([name.text[:-1:].strip(), '-'])
        # elif(name.text[:-1:].strip() == None):
        #     csv_writer.writerow(['-', des.text.strip()])

    for boxx in boxess:
        names = boxx.find('dt')
        print(names.text[:-1:].strip())
        function_name_li.append(names.text[:-1:].strip())

        dess = boxx.find('dd')
        print(dess.text.strip())
        discription_li.append(dess.text.strip())

        try:
            csv_writer.writerow([names.text[:-1:].strip(), dess.text.strip()])
        except Exception as ex:
            print(ex)

        # if(name.text[:-1:].strip() and des.text.strip() != None):
        #     csv_writer.writerow([names.text[:-1:].strip(), dess.text.strip()])
        # elif(des.text.strip() == None):
        #     csv_writer.writerow([names.text[:-1:].strip(), '-'])
        # elif(name.text[:-1:].strip() == None):
        #     csv_writer.writerow(['-', dess.text.strip()])

        # csv_writer.writerow([names.text[:-1:].strip(), dess.text.strip()])


print(links_li)
print(discription_li)
print(function_name_li)
csv_file.close()