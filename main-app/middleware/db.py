from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from icecream import ic

from core import db_helper


class DatabaseMiddleware(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:

        ic(data)

        try:
            session = db_helper.session_getter()
            async with session() as db:
                data["session"] = db
        except Exception as e:
            ic(e)
        finally:
            return await handler(event, data)
