from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_command(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Начало работы'
        ),
        BotCommand(
            command='menu',
            description='Показать клавиатуру возможностей'
        ),
        BotCommand(
            command='cancel',
            description='Сбросить клавиатуру'
        ),
        BotCommand(
            command='get_help',
            description='Информация'
        ),

    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())
