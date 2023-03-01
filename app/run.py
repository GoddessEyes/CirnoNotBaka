import asyncio
import logging

from aiogram import Bot, Dispatcher

from app.config.dev import config
from app.handlers.start import start_router


dispatcher = Dispatcher()


async def main() -> None:
    dispatcher.include_routers(start_router)
    bot = Bot(config.bot_token, parse_mode='HTML')
    await dispatcher.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
