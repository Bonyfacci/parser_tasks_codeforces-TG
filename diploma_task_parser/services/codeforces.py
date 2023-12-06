import json

import requests
from django.db import transaction

from diploma_task_parser.models import Task, Topic


class Codeforces:

    def __init__(self):
        self.url = 'https://codeforces.com/api/problemset.problems/'
        self.tasks = []

    def task_parser(self):
        response = requests.get(self.url)
        data = response.json()

        for i in data['result']['problems']:

            for j in data['result']['problemStatistics']:
                if j['contestId'] == i['contestId'] and j['index'] == i['index']:
                    i['solvedCount'] = j['solvedCount']
                    self.tasks.append(i)

        self.write_json()

    def write_json(self):
        """
        Записи информации в JSON-файл
        """
        with open('tasks.json', 'w', encoding='utf-8') as file:
            json.dump(self.tasks, file, indent=4, ensure_ascii=False)

    def writing_topics_to_database(self):
        # Topic.objects.all().delete()
        for i in self.tasks:
            for topic in i['tags']:
                if not Topic.objects.filter(name=topic).exists():
                    Topic.objects.create(
                        name=topic,
                    )

    def writing_tasks_to_database(self):
        # Task.objects.all().delete()

        for task in self.tasks:
            with transaction.atomic():
                try:
                    existing_task = Task.objects.select_for_update().get(
                        contest_id=task['contestId'],
                        contest_index=task['index']
                    )

                    # Обновление полей существующей задачи
                    existing_task.name = task['name']
                    existing_task.type = task['type']
                    existing_task.points = task.get('points', 0)
                    existing_task.rating = task.get('rating', 0)
                    existing_task.solved_count = task.get('solvedCount', 0)
                    existing_task.save()

                    # Очищаем старые темы и добавляем новые
                    existing_task.category.clear()
                    for tag in task['tags']:
                        topic, created = Topic.objects.get_or_create(name=tag)
                        existing_task.category.add(topic)

                except Task.DoesNotExist:
                    # Если задача не существует, создаем новую
                    model = Task.objects.create(
                        contest_id=task['contestId'],
                        contest_index=task['index'],
                        name=task['name'],
                        type=task['type'],
                        points=task.get('points', 0),
                        rating=task.get('rating', 0),
                        solved_count=task.get('solvedCount', 0),
                    )

                    # Добавляем темы
                    for tag in task['tags']:
                        topic, created = Topic.objects.get_or_create(name=tag)
                        model.category.add(topic)
