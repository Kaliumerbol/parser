import requests
from bs4 import BeautifulSoup

def parser_i(url, teg, u_class):
    # url = url
    source = requests.get(url)
    main_text = source.text
    soup = BeautifulSoup(main_text, "html.parser")
    link = soup.find(teg, {'class': u_class})
    return link.text

print(parser_i('https://habr.com/ru/search/?q=python#h', 'a', 'post__title_link'))

print(parser_i('https://habr.com/ru/search/?target_type=posts&order_by=relevance&q=doker&flow=', 'a', 'post__title_link'))
print(parser_i('https://habr.com/ru/company/mailru/blog/550138/', 'span', 'post__title-text'))

