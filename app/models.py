from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.IntField(pk=True)
    tg_name = fields.TextField()

    def __str__(self) -> str:
        return self.tg_name
