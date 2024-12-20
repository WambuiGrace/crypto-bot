# Install and import the necessary libraries 
"""
    pip install pycoingecko
    pip install python-telegram-bot
"""

from pycoingecko import CoinGeckoAPI
from telegram import Bot
import asyncio
import time


#Track specific cryptocurrencies and their target prices
def price_tracking():
    cg = CoinGeckoAPI()
    targets = {
        'bitcoin' : 97000,
        'ethereum' : 4000,
        'cardano' : 0.8800,
    }

    
    met_targets ={}
    for crypto, crypto_target in targets.items():
        response = cg.get_price(ids=crypto, vs_currencies='usd')
        current_price = response[crypto]['usd']
        target_price = targets[crypto]
        
        #check if it hit the target price
        if current_price >= target_price:
            met_targets[crypto] = current_price
        
    print(met_targets)

    if met_targets:
        message = 'Your targets have been met! \n\n'

        for crypto, crypto_price in met_targets.items():
            current_price = crypto_price
            target_price = targets[crypto]
            message += f'{crypto} \nCurrent price: {current_price} (Target price: {target_price}) \n'
    asyncio.run(telegram_message(message))

# Asynchronous function to send a message via Telegram
async def telegram_message(message):
    bot_token = '7724464432:AAGzaAiH0zwl6MSoasXTbMg6pSuZ1VIP-k0'
    chat_id = '1206150042'
    bot = Bot(token=bot_token)
    await bot.send_message(chat_id=chat_id, text= message)

#Loop to check prices every 4 hours
while True:
    price_tracking()
    time.sleep(14400) #4 hours