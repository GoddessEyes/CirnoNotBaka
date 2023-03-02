from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from app.models import User


start_router = Router()


@start_router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    if message.from_user:
        await User.create(tg_name=message.from_user.full_name)


@start_router.message(Command(commands=['help']))
async def cmd_help(message: Message) -> None:
    await message.answer('Help')
