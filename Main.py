import requests
from bs4 import BeautifulSoup

link = "https://vprognoze.ru/user/umqq/"
responce = requests.get(link).text
print(responce)