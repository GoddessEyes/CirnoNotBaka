from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message


start_router = Router()


@start_router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    if message.from_user:
        await message.answer('Hello')
