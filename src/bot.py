import aiohttp
from aiogram import Bot, Dispatcher

from src.config import settings
from src.handlers import router
from src.logger import logger
from src.state import state


async def on_startup() -> None:
    connector = aiohttp.TCPConnector(
        limit=100,
        limit_per_host=30,
        ttl_dns_cache=300,
    )

    state.session = aiohttp.ClientSession(
        connector=connector,
        timeout=aiohttp.ClientTimeout(total=30),
        raise_for_status=False,
    )

    logger.info("Bot started and session created")


async def on_shutdown() -> None:
    if state.session:
        await state.session.close()
        state.session = None

    logger.info("Bot stopped and session closed")


async def run_bot() -> None:
    bot = Bot(token=settings.telegram_token)
    dp = Dispatcher()

    dp.include_router(router)

    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    logger.info("Bot is starting...")

    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()
