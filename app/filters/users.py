from aiogram.filters import Filter
from aiogram.types import Message

from app.repos.user import UserRepo


class AdminCommandFilter(Filter):
    async def __call__(self, message: Message) -> bool:
        if message.from_user and message.from_user.username:
            user = await UserRepo.get_user_by_tg_username(message.from_user.username)
            if user and user.is_superuser:
                return True
        await message.answer('Эта функция доступна только администраторам :(')
        return False
