from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from filters.chat_types import ChatTypeFilter
import kbds.reply as re_kb


user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))

############################################################
# хендлеры на команды
############################################################

@user_private_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет!!!Я виртуальный помощник!!!!",
                         reply_markup=re_kb.start_kb)

@user_private_router.message(F.text.lower().contains('достав'))
@user_private_router.message(Command('shipping'))
async def cmd_shipping(message: Message):
    await message.answer("Доставка: ")

@user_private_router.message(F.text.lower().contains('меню'))
@user_private_router.message(Command('menu'))
async def cmd_menu(message: Message):
    await message.answer("Вот меню: ",
                         reply_markup=re_kb.del_keyboard)

@user_private_router.message((F.text.lower().contains('инфо')) |
                             (F.text == 'О магазине'))
@user_private_router.message(Command('about'))
async def cmd_about(message: Message):
    await message.answer("О нас: ")

@user_private_router.message(F.text.lower().contains('опла'))
@user_private_router.message(Command('payment'))
async def cmd_payment(message: Message):
    await message.answer("Оплата: ")

##################################################################
# хендлеры на сообщения
##################################################################

@user_private_router.message((F.text.lower().contains('прив')) |
                             (F.text.lower() == 'привет'))
async def helo_response(message: Message):
    await message.answer(f"Сам ты привет, "
                         f"{message.from_user.first_name}, "
                         f"твой ID: {message.from_user.id}!")
