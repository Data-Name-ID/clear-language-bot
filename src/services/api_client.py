import aiohttp

from src.config import settings
from src.logger import logger


async def translate_text(session: aiohttp.ClientSession, text: str) -> str:
    try:
        async with session.post(
            settings.api_url,
            json={"text": text},
            timeout=aiohttp.ClientTimeout(total=20),
        ) as response:
            response.raise_for_status()
            data = await response.json()
            return data["translated_text"]

    except aiohttp.ClientError as e:
        logger.error("Network error communicating with API: %s", e)
        raise
    except Exception:
        logger.exception("Unexpected error occurred")
        raise
