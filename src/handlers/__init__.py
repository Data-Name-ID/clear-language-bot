__all__ = ["router"]

from aiogram import Router

from src.handlers import commands, messages

router = Router()
router.include_router(commands.router)
router.include_router(messages.router)
