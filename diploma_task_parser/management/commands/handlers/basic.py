from aiogram.client import bot
from aiogram.types import Message, ReplyKeyboardRemove

from diploma_task_parser.management.commands.keyboards.topics import get_inline_keyboard, get_inline_keyboard_rating


async def get_menu(message: Message):
    await message.delete()
    await message.answer(f'Привет, {message.from_user.first_name}!'
                         f'\nУ тебя есть варианты: ',
                         reply_markup=get_inline_keyboard())


async def get_cancel(message: Message):
    await message.delete()
    await message.answer(f'Чисто', reply_markup=ReplyKeyboardRemove())


async def get_help(message: Message):
    await message.delete()
    await message.answer(f"Запрос формируется вот так: тема/рейтинг"
                         f"\nПримеры:"
                         f"\nflows/900"
                         f"\nmath/1500"
                         f"\ngames/2200"
                         f"\n\nPython-разработчик - <b>Платонов Сергей</b>!"
                         f"\n<tg-spoiler>Bonyfacci</tg-spoiler>© 2023")


async def hello(message: Message):
    await message.answer(f"<b>И тебе привет!</b> {message.from_user.first_name}!")


async def dice(message: Message):
    await message.delete()
    await message.answer_dice(emoji="🎲")


async def bowling(message: Message):
    await message.delete()
    await message.answer_dice(emoji="🎳")


async def slot_machine(message: Message):
    await message.delete()
    await message.answer_dice(emoji="🎰")


async def dart(message: Message):
    await message.delete()
    await message.answer_dice(emoji="🎯")


async def football(message: Message):
    await message.delete()
    await message.answer_dice(emoji="⚽")


async def basketball(message: Message):
    await message.delete()
    await message.answer_dice(emoji="🏀")
