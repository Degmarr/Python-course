import requests
from bs4 import BeautifulSoup

responce = requests.get('https://automarine.ru/eng/index.html')
print(responce.text)

soup = BeautifulSoup(responce.text, 'html.parser')
# def info():
#     print(soup.title)

# def aboutus():
#     for i in soup.descendants:
#         if i.name:
#             print(i.name)
#     print(soup.text)
#     print(soup.find('div', id = 'about_us')) #attr=(id:'page)

def span():
    first_span = soup.find('span')
    if first_span is not None:
        print(first_span)
    else:
        print("No <span> tag found.")

#info()
#aboutus()
span()
