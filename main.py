from about import about_router
from github import github_router
from discord import discord_router
from steam import steam_router
from start import start_router
from spotify import spotify_router
from bot_token import bot
from aiogram import  Dispatcher, types, Router
from aiogram.filters.command import Command
import asyncio
dp = Dispatcher()
async def main():
    dp.include_router(about_router)
    dp.include_router(github_router)
    dp.include_router(discord_router)
    dp.include_router(steam_router)
    dp.include_router(start_router)
    dp.include_router(spotify_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(main())