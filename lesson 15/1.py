import requests
from bs4 import BeautifulSoup

#responce = requests.get('https://google.com')
#print(responce.text)

#soup = BeautifulSoup(responce.text, 'html.parser')
#print(soup.title)

#titles = soup.selecT('h1', class = "main-header") поиск по селектору
#for title in titles:
#    print(title.text)

responce = requests.get('https://flowerline.shop/')

soup = BeautifulSoup(responce.text, 'html.parser')

for i in soup.descendants:
    if i.name:
        print(i.name)
print(soup.h1.text)
print(soup.find('div', id = 'page')) #attr=(id:'page)

for tag in soup.find_all('h2'):
    print(tag.text)