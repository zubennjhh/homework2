from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


r_kb = InlineKeyboardMarkup()
r_kb.add(InlineKeyboardButton('меню', callback_data='menu'))

async def StoneIsland(message: types.Message):


    photo1 = open('images/4232194418_w640_h640_4232194418.webp', 'rb')
    await message.answer(text='зипка Stonisland')
    await message.answer_photo(photo1)
    await message.answer(text='M', reply_markup=r_kb)



async def carhart(message: types.Message):

    photo2 = open('images/rus_pl_SHAPKA-Carhartt-WIP-Acrylic-Watch-I020222-Black-18855_1.jpg', 'rb')
    await message.answer(text='шапка кархарт ')
    await message.answer_photo(photo2)
    await message.answer(text='XL', reply_markup=r_kb)



async def Arterix(message: types.Message):

    photo3 = open('images/3951938679_w640_h640_3951938679.webp', 'rb')

    await message.answer(text='ветровка arterix')
    await message.answer_photo(photo3)
    await message.answer(text='XXL', reply_markup=r_kb)