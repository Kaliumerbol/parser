import requests
from bs4 import BeautifulSoup


url = 'https://habr.com/ru/search/?q=python#h'

source = requests.get(url)
main_text = source.text
soup = BeautifulSoup(main_text, "html.parser")

link = soup.find('a', {'class': 'post__title_link'})

print(link.text)