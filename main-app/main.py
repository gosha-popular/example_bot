import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from icecream import ic

from core import db_helper
from core import setting
from routers import router

dp = Dispatcher()


async def on_startup():
    pass


async def on_shutdown():
    await db_helper.dispose()


async def main():

    bot = Bot(
        token=setting.bc.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        ic("Exit from program")
