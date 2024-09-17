import asyncio
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

api = '7227838526:AAHuAtKJ3k0NSDANLHGk0A7GbMLT0N9HB6k'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = InlineKeyboardMarkup()
button1 = InlineKeyboardButton(text='Информация', callback_data='info')
kb.add(button1)

menu = ReplyKeyboardMarkup(resize_keyboard=True,
                           keyboard=[
    [KeyboardButton(text='info')],
    [KeyboardButton(text='Куплю'), KeyboardButton(text='Продам')]
                           ])

@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer('Привет! Будем торговать.', reply_markup=kb)

@dp.callback_query_handler(text='info')
async def inlin_but(call):
    await call.message.answer('Это бот Владислава Васильевича. Создан в 2024 году.', reply_markup=menu)
    # await call.answer         # чтобы инлайн-кнопка после выполнения команды становилась кликабельна.
                                # Прикол,но у меня и без этой команды она кликабельна :)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
