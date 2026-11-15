from aiogram import Router, types
from aiogram.filters.command import Command
spotify_router = Router()
@spotify_router.message(Command('spotify'))
async def spotify(message:types.Message):
    text = (
    'Ссылка на профиль spotify: <a href ="https://open.spotify.com/user/31rbyilvtfrgfhcmwq4f6nbknlb4"> нажми сюда</a>'
    )
    await message.answer(text,parse_mode='HTML')