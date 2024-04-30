import requests
from bs4 import BeautifulSoup

response = requests.get('https://intrigue.dating/interesnoe/365-jelaniy-na-kajdyy-den-spisok/')

bs = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')

table = bs.find_all('div', attrs={'class': 'entry-content'})

for i in table:
    vse = i.find_all('li')
    for g in vse:
        dela = g.text
        print(dela)