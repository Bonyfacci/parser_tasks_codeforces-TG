import asyncio
import logging
from aiogram.types import CallbackQuery
from aiogram.utils.formatting import as_list, as_marked_section, Bold
from aiogram.utils.keyboard import InlineKeyboardBuilder

from diploma_task_parser.management.commands.keyboards.topics import get_inline_keyboard_rating
from diploma_task_parser.models import Topic, Task


async def select_topics(call: CallbackQuery):
    try:
        loop = asyncio.get_event_loop()
        topics = await loop.run_in_executor(None, get_inline_keyboard)
        await call.message.answer(f'====='
                                  f'\n<b>Темы:</b>'
                                  f'\n=====',
                                  reply_markup=topics)
        await call.answer()
    except Exception as e:
        logging.error(f"Error in select_topics: {e}")


def get_topics():
    topics = []
    for i in Topic.objects.all():
        topics.append(i.name)
    return '\n'.join(topics)


def get_inline_keyboard():
    topics = get_topics()

    keyboard_builder = InlineKeyboardBuilder()

    for i in topics.split('\n'):
        if i.find(' '):
            keyboard_builder.button(text=i, callback_data=i)
        else:
            keyboard_builder.button(text=i, callback_data=i)

    keyboard_builder.adjust(3)
    return keyboard_builder.as_markup()


async def get_rating(call: CallbackQuery):
    await call.message.answer(
        f'<b>Выберите рейтинг задачи: </b>',
        reply_markup=get_inline_keyboard_rating()
    )
    await call.answer()


async def select_task(call: CallbackQuery):
    topic = call.data

    try:
        loop = asyncio.get_event_loop()
        answer = await loop.run_in_executor(None, get_tasks, topic)

        answer_list = answer.split('\n\n')
        content = as_list(
            as_marked_section(
                Bold(
                    f'Вы выбрали тему:     "{topic}"'
                    f'\nТоп решаемых задач по этой теме:'
                ),
                answer_list[0],
                answer_list[1],
                answer_list[2],
                marker="\n✅ ",
            ),
        )
        await call.message.answer(**content.as_kwargs())
        await call.answer(
            text="Спасибо, что воспользовались моим ботом!",
            show_alert=True
        )
    except Exception as e:
        logging.error(f"Error in select_topics: {e}")


def get_tasks(topic):
    topic = Topic.objects.get(name=topic)
    tasks = []
    for i in Task.objects.all().filter(category=topic.id).order_by('-solved_count')[:3]:
        tasks.append(i.__str__())
    return '\n\n'.join(tasks)
