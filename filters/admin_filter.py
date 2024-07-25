from aiogram.filters import BaseFilter
from aiogram.types import Message

from config import TelegramConfig


class AdminFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id == TelegramConfig.ADMIN_ID
