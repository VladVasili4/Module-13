from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup     #Машина состояний
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio


# api = '7227838526:AAHuAtKJ3k0NSDANLHGk0A7GbMLT0N9HB6k'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


in_kb = InlineKeyboardMarkup()
in_button1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
in_button2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
in_kb.add(in_button1)
in_kb.add(in_button2)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
kb.add(button1)
kb.insert(button2)

gender_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Мужчина', callback_data='man_')],
    [InlineKeyboardButton(text='Женщина', callback_data='woman_')]
])

buy1_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Итого', callback_data='man_formula')]])

buy2_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Итого', callback_data='woman_formula')]])

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    # gender = State()

@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)

@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=in_kb)

@dp.callback_query_handler(text=['calories'])
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.callback_query_handler(text=['formulas'])
async def get_formulas(call):
    await call.message.answer('мужчинам: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5; \n '
                              'женщинам: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')
    # await call.answer         # чтобы инлайн-кнопка после выполнения команды становилась кликабельна.
                                # Hо у меня и без этой команды она кликабельна ?????? !!!!!!)

@dp.callback_query_handler(text=['man_'])
async def male(call):
    await call.message.answer(f'Ура, Вы Мужик!', reply_markup=buy1_kb)
    # await call.answer()

@dp.callback_query_handler(text=['woman_'])
async def female(call):
    await call.message.answer(f'Ура, Вы Дама!', reply_markup=buy2_kb)
    # await call.answer()


@dp.message_handler(text=['Информация'])
async def inform(message):
    await message.answer('Это бот для рассчета калорий, необходимых ежедневно человеку, '
                         'в зависимости от параметров человека')

@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(user_age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(user_growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def set_gender(message, state):
    await state.update_data(user_weight=message.text)
    await message.answer('Укажите свой пол:', reply_markup=gender_kb)

@dp.callback_query_handler(text=['man_formula'])
async def send_calories_man(call, state):
    data = await state.get_data(['user_age', 'user_growth', 'user_weight'])
    count_calories_m = (10.0 * float(data['user_weight']) + 6.25 * float(data['user_growth'])
                      - 5.0 * float(data['user_age']) + 5)
    await call.message.answer(f'Ваша норма калорий : {count_calories_m}')
    await call.answer()

@dp.callback_query_handler(text=['woman_formula'])
async def send_calories_man(call, state):
    data = await state.get_data(['user_age', 'user_growth', 'user_weight'])
    count_calories_m = (10.0 * float(data['user_weight']) + 6.25 * float(data['user_growth'])
                      - 5.0 * float(data['user_age']) - 161)
    await call.message.answer(f'Ваша норма калорий : {count_calories_m}')
    await call.answer()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)