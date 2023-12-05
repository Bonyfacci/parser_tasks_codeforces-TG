from aiogram import Bot
from aiogram.types import Message

from diploma_task_parser.management.commands.keyboards.reply import get_reply_keyboard
from diploma_task_parser.management.commands.utils.commands import set_command


async def start_bot(bot: Bot):
    await set_command(bot)
    await bot.send_message(6534158543, text='Внимание! Бот запущен!')


async def start(message: Message):
    await message.answer(f"Holaaa!"
                         f"\nРад тебя видеть <b>{message.from_user.first_name}</b>!"
                         f"\nПредставляю твоему вниманию Дипломную работу"
                         f"\n===== ВВ4 - Парсер задач =====",
                         reply_markup=get_reply_keyboard())


async def stop_bot(bot: Bot):
    await bot.send_message(6534158543, text='Внимание! Бот выключен!')
