import asyncio
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv('TOKEN_BOT'))

dp = Dispatcher()

ALLOWED_UPDATES = ['message', "edited_message"]


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет!!!Это была команда старт!!!!")

@dp.message(F.text.lower() == 'привет')
async def helo_response(message: Message):
    await message.answer(f"Сам ты привет, {message.from_user.first_name}твой ID: {message.from_user.id}!")

@dp.message()
async def echo(message: Message):
    await message.answer(message.text)










async def main():
    await bot.delete_webhook(drop_pending_updates=True) # сброс присланных сообщений при не запущенном боте
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)






if __name__ == '__main__':
    asyncio.run(main())


