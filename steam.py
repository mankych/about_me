from aiogram import Router, types
from aiogram.filters.command import Command
steam_router = Router()
@steam_router.message(Command('steam'))
async def steam(message: types.Message):
    await message.answer('Ссылка на steam: <a href ="https://steamcommunity.com/profiles/76561199182313223/"> нажми сюда</a>',parse_mode='HTML')