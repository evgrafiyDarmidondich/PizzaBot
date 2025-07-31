from string import punctuation

from aiogram import Router
from aiogram.types import Message

from filters.chat_types import ChatTypeFilter

user_group_router = Router()
user_group_router.message.filter(ChatTypeFilter(['group', 'supergroup']))

restricted_words = {'хуй', 'пизда', 'залупа'}

def clean_text(text: str):
    return text.translate(str.maketrans('', '', punctuation))

@user_group_router.message()
async def mat_del(message: Message):
    if restricted_words.intersection(clean_text(message.text.lower()).split()):
        await message.answer(f"Не ругайся матом!!!{message.from_user.first_name}")
        await message.delete()
