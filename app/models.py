from typing import Self

from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.IntField(pk=True)
    created = fields.DatetimeField(auto_now_add=True)

    tg_id = fields.IntField(unique=True)
    tg_username = fields.CharField(max_length=32, unique=True)
    is_superuser = fields.BooleanField(default=False)

    def __str__(self: Self) -> str:
        return f'{self.tg_id} / {self.tg_username}'
