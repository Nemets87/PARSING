from bs4 import BeautifulSoup
import time
import telebot
import requests
import os
import dotenv

# Load environment variables
dotenv.load_dotenv()

# Constants
TOKEN = os.getenv('TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
URL = 'https://joystick161.ru/products/55959059'
SLEEP_INTERVAL = 60*10  # 10 minutes

# Initialize bot
bot = telebot.TeleBot(TOKEN)


def check_price(previous_price):
    """
    Check the price of a product and send a message if it has changed.
    """
    try:
        r = requests.get(URL)  
        soup = BeautifulSoup(r.text, 'lxml')  
        new_price = soup.find('span', {'class': 'product-price-data'}).get('data-cost')
    except Exception as e:
        print(f"An error occurred: {e}")
        return previous_price

    if previous_price != new_price:
        try:
            bot.send_message(CHAT_ID, 'Price changed: ' + new_price)
        except Exception as e:
            print(f"An error occurred: {e}")
        else:
            previous_price = new_price

    return previous_price


def main():
    """
    Main function that checks the price every 10 minutes.
    """
    previous_price = ''
    while True:
        previous_price = check_price(previous_price)
        time.sleep(SLEEP_INTERVAL)


if __name__ == "__main__":
    main()