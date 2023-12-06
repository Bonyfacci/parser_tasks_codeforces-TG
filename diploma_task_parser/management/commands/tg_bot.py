import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from django.core.management import BaseCommand

from aiogram.filters.command import Command as TGCommand

from diploma_task_parser.management.commands.handlers.basic import hello, \
    get_help, dice, bowling, slot_machine, dart, football, basketball, get_menu, get_cancel
from diploma_task_parser.management.commands.handlers.callback import select_topics, select_task
from diploma_task_parser.management.commands.handlers.start_stop import start_bot, stop_bot, start
from diploma_task_parser.management.commands.handlers.top_5_tasks import get_top_5_solved, get_top_5_rating, \
    get_top_5_points
from diploma_task_parser.management.commands.handlers.topic_and_rating import get_topic_rating


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        asyncio.run(self.start())

    async def start(self):
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - [%(levelname)s] - %(name)s - "
                   "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
        )
        bot = Bot(token="6951316725:AAGHFJKP1CNumDSA9vT4hXdC5BBb2PV5dQE", parse_mode='HTML')

        dp = Dispatcher()

        dp.message.register(start, TGCommand("start"))
        dp.message.register(get_help, TGCommand("get_help"))

        dp.message.register(hello, F.text == "Привет")

        dp.message.register(get_menu, F.text == "Начать работу!")

        dp.message.register(get_menu, TGCommand("menu"))
        dp.message.register(get_cancel, TGCommand("cancel"))

        dp.callback_query.register(select_topics, F.data.startswith('topics'))

        dp.callback_query.register(get_top_5_solved, F.data.startswith('top_5_solved'))
        dp.callback_query.register(get_top_5_rating, F.data.startswith('top_5_rating'))
        dp.callback_query.register(get_top_5_points, F.data.startswith('top_5_points'))

        dp.callback_query.register(select_task)

        dp.message.register(dice, F.text == "Кинуть кубик")
        dp.message.register(bowling, F.text == "Боулинг")
        dp.message.register(slot_machine, F.text == "Рулетка")
        dp.message.register(dart, F.text == "Дартс")
        dp.message.register(football, F.text == "Футбол")
        dp.message.register(basketball, F.text == "Баскетбол")

        try:
            dp.message.register(get_topic_rating)
        except Exception as e:
            print(e)

        dp.startup.register(start_bot)
        dp.shutdown.register(stop_bot)

        try:
            await dp.start_polling(bot)
        finally:
            await bot.session.close()
