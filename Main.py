from itertools import tee
from turtle import title
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

URL_TEMPLATE = "https://vprognoze.ru"
r = requests.get(URL_TEMPLATE)
print(r.status_code)

print(r.text)

# soup = bs(r.text, "html.parser")
# vacancies_names = soup.find_all('div', class_='section__body')
# for name in vacancies_names:
#     print(name.a['title'])