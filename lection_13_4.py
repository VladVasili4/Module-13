import asyncio
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

api = '7227838526:AAHuAtKJ3k0NSDANLHGk0A7GbMLT0N9HB6k'
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())


class UserState(StatesGroup):
    adress = State()


@dp.message_handler(text=['Заказ'])
async def buy(message):
    await message.answer('Укажите адрес доставки')
    await UserState.adress.set()

@dp.message_handler()
async def all_message(message):
    await message.answer(f' Хватит писать всякую чушь, набери "Заказ" (без ковычек)')

@dp.message_handler(state=UserState.adress)
async def fsm_handler(message, state):
    await state.update_data(user_adress=message.text) # user_adress - может быть любое значение
    data = await state.get_data('user_adress')
    print(data)
    await message.answer(f'Заказ будет доставлен по адресу: {data["user_adress"]}')

    await state.finish()




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)