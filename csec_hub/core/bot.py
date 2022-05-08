import os
import re

API_KEY = os.getenv("TG_API_KEY")
SUBSCRIBERS_CHANAL = os.getenv("SUBSCRIBERS_CHANAL")


from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup


def send_to_subscribers(feed):
    bot = Bot(API_KEY)
    button = [[InlineKeyboardButton("Like", callback_data="like")]]
    markup = InlineKeyboardMarkup(button)
    new = f"""
            user : {feed.title}
            title : {feed.title}
            
        """
    bot.send_message(SUBSCRIBERS_CHANAL, new, reply_markup=markup)

    return