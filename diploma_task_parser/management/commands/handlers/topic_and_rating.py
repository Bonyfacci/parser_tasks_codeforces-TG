import asyncio

from aiogram.types import Message
from aiogram.utils.formatting import as_list, as_marked_section, Bold

from diploma_task_parser.models import Topic, Task


async def get_topic_rating(message: Message):
    loop = asyncio.get_event_loop()
    topic_db = await loop.run_in_executor(None, get_topics)

    topic_list = topic_db.split(',')

    if '/' in message.text:
        data = message.text.lower().split('/')
        if data[0] in topic_list:
            query = {'topic': data[0], 'rating': data[1]}

            loop = asyncio.get_event_loop()
            task_db = await loop.run_in_executor(None, get_tasks, query)

            answer_list = task_db.split('\n\n')
            content = as_list(
                as_marked_section(
                    Bold(
                        f'Вы выбрали тему:     {query["topic"]}'
                        f'\nВы выбрали рейтинг:     {query["rating"]}'
                        f'\nТоп решаемых задач по этой теме:'
                    ),
                    answer_list[0],
                    answer_list[1],
                    answer_list[2],
                    marker="\n✅ ",
                ),
            )
            await message.answer(**content.as_kwargs())
        else:
            await message.answer(f'Я не знаю такой команды!')
    else:
        await message.answer(f'Я не знаю такой команды!')


def get_topics():
    topics = []
    for i in Topic.objects.all():
        topics.append(i.name)
    return ','.join(topics)


def get_tasks(query):
    topic = Topic.objects.get(name=query['topic'])
    tasks = []
    for i in Task.objects.all().filter(category=topic.id).filter(rating=query['rating']).order_by('-solved_count')[:3]:
        tasks.append(i.__str__())
    return '\n\n'.join(tasks)
