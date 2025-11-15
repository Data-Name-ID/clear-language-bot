from aiogram import Router
from aiogram.types import Message

from src.logger import logger
from src.services import translate_text
from src.state import state

router = Router()


@router.message()
async def handle_message(message: Message) -> None:
    if not message.text or not message.from_user:
        return

    user_message = message.text
    logger.info(
        "Received message from %s: %s",
        message.from_user.id,
        user_message,
    )

    if not state.session:
        await message.answer("Бот еще не готов, попробуйте позже.")
        return

    try:
        ai_reply = await translate_text(state.session, user_message)
    except Exception:
        ai_reply = "Извините, произошла ошибка при обработке вашего запроса."

    await message.answer(ai_reply)
