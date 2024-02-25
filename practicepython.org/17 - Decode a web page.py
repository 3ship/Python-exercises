# 17 Decode a web page with requests and BeautifulSoup

import requests
from bs4 import BeautifulSoup

url = requests.get('http://www.welt.de')
url_html = url.text

titleList = []

soup = BeautifulSoup(url_html, 'html.parser')
for header in soup.find_all('h4'):
    try:
        for title in header.find_all('a'):
            titleList.append(title.get('aria-label'))
    except: continue

filter = ['Brand Story',
          'Deals (neu)',
          'Livestream (Artikel enthält Videos)',
          'Live-TV (Artikel enthält Videos)',
          'LIVESTREAM (Artikel enthält Videos)',
          'Video (Artikel enthält Videos)',
          'Aktienkurs:']

def fileName(name):
    try:
        output = open(name, 'x')
    except FileExistsError:
        print('The file already exists!')
        fileName(input('Enter an alternative file name: '))
    else:
        createFile(output)

def createFile(name):
    for element in titleList:
        if any(keyword in element for keyword in filter):
            continue
        else:
            name.write(element + '\n')

if __name__=="__main__":
    query = input('Enter file name for output: ')
    fileName(query)