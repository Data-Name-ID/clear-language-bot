from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def start(message: Message) -> None:
    await message.answer(
        "Привет! Отправь мне текст и я переведу его на Ясный язык.",
    )


@router.message(Command("help"))
async def help_command(message: Message) -> None:
    help_text = """Привет! 👋

Я — твой помощник по переводу сложных текстов на ясный и понятный язык.
Моя задача — сделать информацию доступной и легкой для восприятия.

Если у тебя есть текст, который ты хочешь упростить, просто отправь его мне,
и я помогу сделать его более понятным 😊

Давай сделаем общение проще вместе!"""
    await message.answer(help_text)
