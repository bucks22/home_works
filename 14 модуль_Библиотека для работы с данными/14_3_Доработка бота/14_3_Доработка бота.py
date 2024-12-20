from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

kb_start = ReplyKeyboardMarkup(resize_keyboard=True)
but1 = KeyboardButton(text = 'Рассчитать')
but2 = KeyboardButton(text= 'Информация')
but3 = KeyboardButton(text= 'Купить')
kb_start.row(but1, but2)
kb_start.add(but3)

kb_inline = InlineKeyboardMarkup(resize_keyboard=True)
but1 = KeyboardButton(text = 'Рассчитать норму калорий', callback_data='calories')
but2 = KeyboardButton(text= 'Формулы расчёта', callback_data='formulas')
kb_inline.row(but1, but2)

kb_products = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text= 'Product1', callback_data="product_buying"),
        InlineKeyboardButton(text= 'Product2', callback_data="product_buying"),
        InlineKeyboardButton(text= 'Product3', callback_data="product_buying"),
        InlineKeyboardButton(text= 'Product4', callback_data="product_buying")
    ]
    ], resize_keyboard=True)

@dp.message_handler(commands = ['start'])
async def start(message):
    await message.answer('Привет!', reply_markup = kb_start)

@dp.message_handler(text = 'Купить')
async def get_buying_list(message):
    for i in range (4):
        await message.answer(f'Название: Product{i+1} | Описание: описание {i+1} | Цена: {(i+1) * 100}')
        with open (f'{i+1}.jpg', 'rb') as img:
            await message.answer_photo(img)
    await message.answer(text= 'Выберите продукт для покупки:', reply_markup = kb_products)

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!', reply_markup = kb_start)


@dp.message_handler(text = 'Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию: ', reply_markup=kb_inline)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()

@dp.callback_query_handler(text = 'calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст: ')
    await UserState.age.set()

@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(age = message.text)
    await message.answer('Введите свой рост: ')
    await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес: ')
    await UserState.weight.set()

@dp.message_handler(state = UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    calories = 10 * int(data['weight']) + 6.25 * int(data['growth']) + 5 * int(data['age']) + 5
    await message.answer(f'Норма калорий: {calories}')
    await state.finish()

# @dp.message_handler()
# async def all_message(message):
#     await message.answer("Введите команду /start, чтобы начать общение.")
#     # print("Введите команду /start, чтобы начать общение.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

