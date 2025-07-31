import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommandScopeAllPrivateChats
from dotenv import load_dotenv

from common.bot_cmds_list import private
from handlers.user_group import user_group_router
from handlers.user_private import user_private_router


ALLOWED_UPDATES = ['message', "edited_message"]
load_dotenv()

bot = Bot(token=os.getenv('TOKEN_BOT'))

dp = Dispatcher()

dp.include_routers(
    user_private_router,
    user_group_router,

)



async def main():
    # сброс присланных сообщений при не запущенном боте
    await bot.delete_webhook(drop_pending_updates=True)

    dp.startup.register(startup)
    dp.shutdown.register(shutdown)

    await bot.set_my_commands(commands=private,
                              scope=BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot,
                           allowed_updates=ALLOWED_UPDATES)



async def startup(dispatcher: Dispatcher):
    print('Бот запущен')

async def shutdown(dispatcher: Dispatcher):
    print('Бот остановлен')

if __name__ == '__main__':
    asyncio.run(main())


