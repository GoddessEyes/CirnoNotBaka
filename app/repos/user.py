from tortoise.exceptions import DoesNotExist

from app.models import User
from app.types_alias import TgUser


class UserRepo:
    @staticmethod
    async def get_first_admin_account() -> User | None:
        return await User.filter(is_superuser=True).order_by('created').first()

    @staticmethod
    async def create_user(*, tg_user: TgUser, is_superuser: bool) -> tuple[User, bool]:
        return await User.get_or_create(
            tg_id=tg_user.id,
            defaults={'tg_username': tg_user.username, 'is_superuser': is_superuser},
        )

    @staticmethod
    async def get_user_by_tg_username(tg_username: str) -> User | None:
        try:
            return await User.get(tg_username=tg_username)
        except DoesNotExist:
            return None
