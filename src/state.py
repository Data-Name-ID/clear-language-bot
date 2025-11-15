from dataclasses import dataclass

import aiohttp


@dataclass
class BotState:
    session: aiohttp.ClientSession | None = None


state = BotState()
