from aiogram import Router, types
from aiogram.filters.command import Command
discord_router = Router()
@discord_router.message(Command('discord'))
async def discord(message:types.Message):
    text = (
        'Имя профиля discord: <b> redman35</b>\n'
        'Ссылка профиля discord: <a href="https://discord.com/users/redman35"> нажми тут </a>'    )
    await message.answer(text,parse_mode='HTML')