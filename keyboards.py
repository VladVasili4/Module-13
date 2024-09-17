from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



in_kb = InlineKeyboardMarkup(inline_keyboard=[
    [KeyboardButton(text='Для начинающих',callback_data='small')],
    [KeyboardButton(text='Для опытных',callback_data='medium')],
    [KeyboardButton(text='Для профи',callback_data='big')],
    [KeyboardButton(text='Другие предложения',callback_data='other')]])


start_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='О нас')],
    [KeyboardButton(text='Стоимость')]],
                           resize_keyboard=True)


buy_kb = InlineKeyboardMarkup(inline_keyboard=[[KeyboardButton(text='Купить', url='https://ya.ru/')],
                                               [KeyboardButton(text='Назад', callback_data='back_to_catalog')]])