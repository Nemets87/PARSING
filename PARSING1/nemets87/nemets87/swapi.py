from bs4 import BeautifulSoup

import time
import telebot
import requests
import os

import dotenv


dotenv.load_dotenv()


TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN) 
CHAT_ID = os.getenv('CHAT_ID')

url = 'https://joystick161.ru/products/55959059'  
previous_price = ''


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


while True:
    check_price()
    time.sleep(60*10)
