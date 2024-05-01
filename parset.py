import requests
import random
from bs4 import BeautifulSoup

url = 'https://intrigue.dating/interesnoe/365-jelaniy-na-kajdyy-den-spisok/'

def parser(url):
    response = requests.get(url)

    bs = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')

    table = bs.find_all('div', attrs={'class': 'entry-content'})
    for i in table:
        dela = i.find_all('li')
        return [c.text for c in dela]

list_of_del = parser(url)
random.shuffle(list_of_del)