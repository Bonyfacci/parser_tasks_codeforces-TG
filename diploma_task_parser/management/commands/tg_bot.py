from asgiref.sync import sync_to_async
from django.core.management import BaseCommand

import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command as TGCommand

from diploma_task_parser.models import Topic


class Command(BaseCommand):

    def __init__(self):
        super().__init__()

        # Включаем логирование, чтобы не пропустить важные сообщения
        logging.basicConfig(level=logging.INFO)
        # Объект бота
        self.bot = Bot(token="6951316725:AAGHFJKP1CNumDSA9vT4hXdC5BBb2PV5dQE")
        # Диспетчер
        self.dp = Dispatcher()

        self.dp["content"] = self.get_topics()

    def handle(self, *args, **kwargs):

        # Хэндлер на команду /start
        @self.dp.message(TGCommand("start"))
        async def cmd_start(message: types.Message):
            await message.answer("Hello!")

        @self.dp.message(TGCommand("topic"))
        async def cmd_topic(message: types.Message, content):
            await message.answer(f"Темы {content}")

        asyncio.run(self.main())

    @sync_to_async
    def get_topics(self):
        my_list = list(Topic.objects.all().values('name'))
        return my_list

    # Запуск процесса поллинга новых апдейтов
    async def main(self):
        await self.dp.start_polling(self.bot)
