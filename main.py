from aiogram import Bot, Dispatcher, executor
from dotenv import load_dotenv
from os import getenv
from aiogram.dispatcher.filters import Text

'''импорт функций'''
from handlers.answer import qwerty
from handlers.start import start_command
from handlers.menu2 import menu
from handlers.adress import adress
from handlers.menu import StoneIsland
from handlers.menu import carcart
from handlers.menu import Arterix


load_dotenv()
bot = Bot(getenv('TG_TOKEN'))
dp = Dispatcher(bot)


dp.register_message_handler(start_command, commands=['start'])
dp.register_callback_query_handler(menu, text='menu')
dp.register_callback_query_handler(adress, text='adress')
dp.register_message_handler(StoneIsland, Text(equals='StoneIsland'))
dp.register_message_handler(carcart, Text(equals='carcart'))
dp.register_message_handler(Arterix, Text(equals='Arterix'))
dp.register_message_handler(qwerty)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)