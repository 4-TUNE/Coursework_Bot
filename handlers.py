from aiogram import types

# імпортуємо бібліотеку aiohttp
import aiohttp

# імпортуємо всі дані з utils
from utils import *

# обробник команди /start
async def start(message: types.Message):

    await message.answer("Привіт!\nОбери бажану монету, щоб дізнатись ціну на неї\n(Надішли акронім)\n BTC\n  LTC\n   ZEC\n    DOGE\n     DASH")

# обробник команди /help
async def help(message: types.Message):

    await message.answer("Доступні криптовалюти:\n" + "\n".join(networks))

    # обробник запиту ціни
async def get_price(message: types.Message):
    network = message.text.upper()  # приводимо повідомлення до верхнього регістру

    # виконуємо перевірку
    if network not in networks:

        await message.answer("Нажаль, ця валюта відсутня для можливості відслідкування")

        return
    session = aiohttp.ClientSession()

    # створюємо GET запит по закріпленому за методом get_price url
    async with session.get(BASE_URL + f"get_price/{message.text}/USD") as resp:

    # отримуємо відповідь у форматі json
        data = await resp.json()

    # якщо статус запиту — успішний
    if data["status"] == "success":

    # розраховуємо ціну і відправляємо користувачу
        price = calculate_price(data)

        await message.answer(price)

    else:

        # сповіщуємо про те, що виникла помилка
        await message.answer("Сталась помилка")