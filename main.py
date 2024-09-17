from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

import logging

from config import *
from keyboards import *
import texts

# api = '7227838526:AAHuAtKJ3k0NSDANLHGk0A7GbMLT0N9HB6k'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer(f'Здравствуйте, {message.from_user.username}, ' + texts.start, reply_markup=start_kb)


# message.answer_photo
# message.answer_video
# message.answer_file
@dp.message_handler(text='О нас')
async def info(message):
    with open('Tiger.jpg', 'rb') as img:
        await message.answer_photo(img, texts.about)

@dp.message_handler(text='Стоимость')
async def price(message):
    await message.answer(texts.vibor, reply_markup=in_kb)

@dp.callback_query_handler(text=['small'])
async def buy_M(call):
    await call.message.answer(texts.Mgame, reply_markup=buy_kb)
    await call.answer()

@dp.callback_query_handler(text=['medium'])
async def buy_L(call):
    await call.message.answer(texts.Lgame, reply_markup=buy_kb)
    await call.answer()

@dp.callback_query_handler(text=['big'])
async def buy_XL(call):
    await call.message.answer(texts.XLgame, reply_markup=buy_kb)
    await call.answer()

@dp.callback_query_handler(text=['other'])
async def buy_other(call):
    await call.message.answer(texts.other, reply_markup=buy_kb)
    await call.answer()

@dp.callback_query_handler(text=['back_to_catalog'])
async def back(call):
    pass


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)