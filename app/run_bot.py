import asyncio
import logging

from aiogram import Bot, Dispatcher
from tortoise import Tortoise

from app.config.dev import TORTOISE_ORM, config
from app.handlers.register import register_router
from app.handlers.start import start_router


db = Tortoise()
dispatcher = Dispatcher()


@dispatcher.startup()
async def startup() -> None:
    await db.init(config=TORTOISE_ORM)


@dispatcher.shutdown()
async def shutdown() -> None:
    await db.close_connections()


async def main() -> None:
    dispatcher.include_routers(start_router, register_router)
    bot = Bot(config.bot_token, parse_mode='HTML')
    await dispatcher.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
