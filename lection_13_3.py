"""
"C:\Users\Ната\PycharmProjects\pythonProject\.venv\lib\site-packages\aiogram"
"""

import asyncio
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage


api = '7227838526:AAHuAtKJ3k0NSDANLHGk0A7GbMLT0N9HB6k'
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

@dp.message_handler(text=['pop', 'kok', 'sos'])
async def text_message(message):
    print('Привет! Что-то из трех букв, посередине "о"? Прикольно')
    await message.answer('Привет! Что-то из трех букв, посередине "о"? Прикольно')

@dp.message_handler(commands=['start'])
async def start_message(message):
    print('Привет! Я бот помогающий твоему здоровью.')
    await message.answer('Стартанул? Тогда поехали :)')

@dp.message_handler()
async def all_message(message):
    print('Введите команду /start, чтобы начать общение.')
    await message.answer(f' Вы ввели : {message.text.upper()}')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
