from aiogram import Router, types
from aiogram.filters.command import Command
github_router = Router()
@github_router.message(Command('github'))
async def github(message:types.Message):
    text = (
        'Ссылка профиля github: <a href="https://github.com/mankych"> нажми тут </a>'    )
    await message.answer(text,parse_mode='HTML')