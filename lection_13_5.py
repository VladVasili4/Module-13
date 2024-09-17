import asyncio
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

api = '7227838526:AAHuAtKJ3k0NSDANLHGk0A7GbMLT0N9HB6k'
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text='Информация')#, , is_persistent=True)
button2 = KeyboardButton(text='Начало')#, resize_keyboard=True, is_persistent=True)
kb.add(button1)
kb.insert(button2)                             # kb.row, kb.insert


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Стартанул? Тогда поехали :)', reply_markup=kb)

@dp.message_handler(text=['Информация'])
async def inform(message):
    await message.answer('Это бот Владислава Васильевича. Создан в 2024 году.')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)