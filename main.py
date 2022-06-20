from aiogram import Bot, Dispatcher, executor
import handlers
API_TOKEN = ''

 #створюємо бота та диспетчер
bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)
 #реєструємо функції
dp.register_message_handler(handlers.start, commands=["start"])

dp.register_message_handler(handlers.help, commands=["help"])

dp.register_message_handler(handlers.get_price)

 #запускаємо програму
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
 #команда пропустить запити надіслані до початку роботи боту