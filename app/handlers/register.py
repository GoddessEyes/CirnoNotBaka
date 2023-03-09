from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.filters.admin import AdminCommandFilter
from app.services.register import RegisterService


register_router = Router()


@register_router.message(Command(commands='i_admin'))
async def create_first_admin(message: Message) -> Message:
    if not message.from_user:
        return await message.answer('Мне кажется с вами что-то не так...')
    user, is_created = await RegisterService.get_or_create_first_admin(tg_user=message.from_user)
    if is_created:
        answer_msg = f'Поздравляю! Первый аккаунт администратора создан!' f'Username: @{user.tg_username}'
    else:
        answer_msg = f'Аккаунт администратора уже существует. Свяжитесь с @{user.tg_username}'
    return await message.answer(answer_msg)


@register_router.message(Command(commands='add_admin'), AdminCommandFilter())
async def set_superuser_to_registered_user(message: Message) -> Message:
    if not message.from_user or not message.text:
        return await message.answer('Проверьте, что вы не ошиблись в формате /add_admin @username')

    tg_username = RegisterService.try_parse_username_args(message.text)
    if not tg_username:
        return await message.answer('Не удалось распознать имя юзера. Проверьте формат: \n /add_admin @username')

    updated_user = await RegisterService.try_set_superuser_by_tg_username(tg_username)
    if not updated_user:
        return await message.answer('Я не смогла отыскать пользователя с таким именем...')
    return await message.answer(f'Пользователь {updated_user.tg_username} получил права администратора!')
