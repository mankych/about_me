from aiogram import Router, types
from aiogram.filters.command import Command
about_router = Router()
@about_router.message(Command('about'))
async def about(message: types.Message):
    text = (
    "👋 <b>Обо мне</b>\n\n"
        "Я Python-разработчик.\n"
        "Пишу парсеры, ботов и автоматизирую задачи.\n\n"
        "🛠 <b>Навыки:</b>\n"
        "• Python\n"
        "• Playwright\n"
        "• SQLite\n"
        "• FastAPI\n"
        "• aiogram\n\n"
        "📂 <b>Проекты:</b>\n"
        "• Парсер 3 маркетплейсов\n")
    await message.answer(text,parse_mode='HTML')