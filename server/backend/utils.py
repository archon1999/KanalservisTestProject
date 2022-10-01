import requests
from bs4 import BeautifulSoup


def parse_ruble_exchange_rate(html):
    soup = BeautifulSoup(html, 'lxml')
    for tr_tag in soup.find(class_='data').find_all('tr')[1:]:
        if tr_tag.find_all('td')[1].text.strip() == 'USD':
            text = tr_tag.find_all('td')[4].text.strip()
            return float(text.replace(',', '.'))


def get_ruble_exchange_rate():
    url = 'https://www.cbr.ru/currency_base/daily/'
    response = requests.get(url)
    if response.ok:
        html = response.text
        return parse_ruble_exchange_rate(html)
