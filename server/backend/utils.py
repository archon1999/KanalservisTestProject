import os

import requests
from bs4 import BeautifulSoup
from telebot import TeleBot


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


def send_notification_about_expiration(order):
    bot = TeleBot(token=os.getenv('TELEGRAM_BOT_TOKEN'))
    text = f'''
⚠️ <b>Уведомление о просрочке:</b>

🧾 <i>Информация про заказ</i>

<b>ℹ️ Номер заказа:</b> <i>{order.order_id}</i>
<b>💲 Стоимость:</b> <i>{order.cost}$</i>
<b>📅 Срок доставки:</b> <i>{order.delivery_time}</i>
'''
    chat_id = os.getenv('TELEGRAM_USER_ID')
    bot.send_message(chat_id, text,
                     parse_mode='HTML')
