from aiogram import Router, types
from aiogram.filters.command import Command
start_router = Router()

@start_router.message(Command('start'))
async def start(message:types.Message):
    text = (
    'Я бот созданный великим манки.\n'
    'Я служу для того чтобы вы узнали о моем хозяине чуть больше\n'
    'Список команд:\n\n'
    '<b>/about</b> - узнать о увлечениях и интересах манки\n'
    '<b>/spotify</b> - получить ссылку на профиль spotify\n'
    '<b>/discord</b> - получить ссылку и юз профиля discord\n'
    '<b>/steam</b> -  получить ссылку профиля steam\n'
    '<b>/github</b> - получить ссылку профиля github'
    )
    
    await message.answer(text,parse_mode='HTML')