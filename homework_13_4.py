from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

api = '123'
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')

@dp.message_handler(text=['Calories'])
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(user_age=message.text)
    # data = await state.get_data()
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(user_growth=message.text)
    # data = await state.get_data()
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(user_weight=message.text)
    data = await state.get_data(['user_age', 'user_growth', 'user_weight'])
    count_calories = (10.0 * float(data['user_weight']) + 6.25 * float(data['user_growth'])
                      - 5.0 * float(data['user_age']) + 5)
    await message.answer(f'Ваша норма калорий : {count_calories} ')
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)