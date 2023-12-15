Друзья,доброго времени суток !
перед вами самый простой БОТ для парсинга сайта 
https://joystick161.ru
который создан в учебных целях для парсига цены игры по адресу:
https://joystick161.ru/products/55959059

он использует библиотеки

from bs4 import BeautifulSoup

import time
import telebot
import requests
import os
import dotenv

чат_айди и токен скрыты в файле .env


dotenv.load_dotenv()


TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)
CHAT_ID = os.getenv('CHAT_ID')

url = 'https://joystick161.ru/products/55959059'
previous_price = ''

основная логика работы скрыта в функции 

def check_price():
    global previous_price
    r = requests.get(url)  
    soup = BeautifulSoup(r.text, 'lxml')  
    new_price = soup.find(
        'span', {'class': 'product-price-data'}).get('data-cost'
                                                     )
    if previous_price != new_price:
        bot.send_message(CHAT_ID, 'Price changed: ' + new_price)
        previous_price = new_price

чекаем страницу каждый час - чтобы не получить бан 
часик в радость - бан не в радость !


while True:
    check_price()
    time.sleep(60*10)

