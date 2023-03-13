from more_itertools import last

from app.models import User
from app.repos.user import UserRepo
from app.types_alias import TgUser


class RegisterService:
    @staticmethod
    async def create_user_from_tg_user(
        tg_user: TgUser,
    ) -> tuple[User, bool]:
        return await UserRepo.create_user(tg_user=tg_user, is_superuser=False)

    @staticmethod
    async def get_or_create_first_admin(tg_user: TgUser) -> tuple[User, bool]:
        """-> User, created?"""
        admin_account = await UserRepo.get_first_admin_account()
        if admin_account:
            return admin_account, False
        return await UserRepo.create_user(tg_user=tg_user, is_superuser=True)

    @staticmethod
    async def try_set_superuser_by_tg_username(tg_username: str) -> User | None:
        user = await UserRepo.get_user_by_tg_username(tg_username)
        if user:
            user.is_superuser = True
            await user.save()
            return user
        return None

    @staticmethod
    def try_parse_username_args(text: str) -> str | None:
        """@username -> username"""
        try:
            username = last(text.split())
            if username.startswith('@'):
                return username[1:]
        except IndexError:
            return None
        return None
