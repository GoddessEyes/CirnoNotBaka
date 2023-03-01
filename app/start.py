import asyncio
import logging

from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command
from aiogram.types import Message

from app.config.dev import config


router = Router()
dispatcher = Dispatcher()


@router.message(Command(commands=['start']))
async def command_start_handler(message: Message) -> None:
    if message.from_user:
        await message.answer(f'Hello, <b>{message.from_user.full_name}!</b>')


async def main() -> None:
    dispatcher.include_router(router)
    bot = Bot(config.bot_token, parse_mode='HTML')
    await dispatcher.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
