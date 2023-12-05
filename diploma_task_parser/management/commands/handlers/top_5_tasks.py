import asyncio
import logging

from aiogram.types import CallbackQuery
from aiogram.utils.formatting import as_list, as_marked_section, Bold

from diploma_task_parser.models import Task


async def get_top_5_solved(call: CallbackQuery):
    try:
        loop = asyncio.get_event_loop()
        answer = await loop.run_in_executor(None, get_top_5_solved_task)
        answer_list = answer.split('=')
        content = as_list(
            as_marked_section(
                Bold("Задачи:"),
                answer_list[0],
                answer_list[1],
                answer_list[2],
                answer_list[3],
                answer_list[4],
                marker="\n✅ ",
            ),
        )
        await call.message.answer(**content.as_kwargs())
        await call.answer()
    except Exception as e:
        logging.error(f"Error in select_topics: {e}")


def get_top_5_solved_task():
    tasks = []
    for i in Task.objects.all().order_by('-solved_count')[:5]:
        tasks.append(i.__str__())
    return '='.join(tasks)


async def get_top_5_rating(call: CallbackQuery):
    try:
        loop = asyncio.get_event_loop()
        answer = await loop.run_in_executor(None, get_top_5_rating_task)
        answer_list = answer.split('=')
        content = as_list(
            as_marked_section(
                Bold("Задачи:"),
                answer_list[0],
                answer_list[1],
                answer_list[2],
                answer_list[3],
                answer_list[4],
                marker="\n✅ ",
            ),
        )
        await call.message.answer(**content.as_kwargs())
        await call.answer()
    except Exception as e:
        logging.error(f"Error in select_topics: {e}")


def get_top_5_rating_task():
    tasks = []
    for i in Task.objects.all().order_by('-rating')[:5]:
        tasks.append(i.__str__())
    return '='.join(tasks)


async def get_top_5_points(call: CallbackQuery):
    try:
        loop = asyncio.get_event_loop()
        answer = await loop.run_in_executor(None, get_top_5_point_task)
        answer_list = answer.split('=')
        content = as_list(
            as_marked_section(
                Bold("Задачи:"),
                answer_list[0],
                answer_list[1],
                answer_list[2],
                answer_list[3],
                answer_list[4],
                marker="\n✅ ",
            ),
        )
        await call.message.answer(**content.as_kwargs())
        await call.answer()
    except Exception as e:
        logging.error(f"Error in select_topics: {e}")


def get_top_5_point_task():
    tasks = []
    for i in Task.objects.all().order_by('-points')[:5]:
        tasks.append(i.__str__())
    return '='.join(tasks)
