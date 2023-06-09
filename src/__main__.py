from os import environ
from sys import stderr

from disnake import Game, Intents
from loguru import logger

from src.core.bot import Bot
from src.utils import CONFIG

from . import __version__


def main() -> None:
    logger.remove()
    level = CONFIG.python.log_level.upper() or "INFO"
    logger.add(stderr, level=level)
    logger.add("logs/file_{time}.log", level="TRACE")

    bot = Bot(
        activity=Game(name=f"Version {__version__}"),
        command_prefix=CONFIG.bot.prefix,
        intents=Intents.all(),
    )

    for ext in [
        "src.exts.commands",
        "src.exts.utils",
        "src.exts.listeners",
    ]:
        bot.load_extension(ext)

    bot.run(environ["DISCORD_TOKEN"])


if __name__ == "__main__":
    main()
