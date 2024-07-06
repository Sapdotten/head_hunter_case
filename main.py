import asyncio

from aiogram import Bot, Dispatcher
from bot.handlers import start
from aiogram.client.session.aiohttp import AiohttpSession
import logging
from utils.settings import Settings
logging.basicConfig(level=logging.INFO)
def register_routers(dp):
    dp.include_routers(start.router)


async def main() -> None:
    """
    Entry point
    """
    # load_environ()
    Settings.load_data_from_file()
    
    session = AiohttpSession()
    bot = Bot(Settings.get_token(), session=session)
    start.register_bot(bot)
    dp = Dispatcher()
    register_routers(dp)
    try:
        await bot.delete_webhook()
        await dp.start_polling(bot)
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    asyncio.run(main())