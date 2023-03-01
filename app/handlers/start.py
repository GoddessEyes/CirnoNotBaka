from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message


start_router = Router()


@start_router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    if message.from_user:
        await message.answer(f'Hello, <b>{message.from_user.full_name}!</b>')


@start_router.message(Command(commands=['help']))
async def cmd_help(message: Message) -> None:
    await message.answer('Help')
