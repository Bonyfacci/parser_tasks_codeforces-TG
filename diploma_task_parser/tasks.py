from celery import shared_task

from diploma_task_parser.services.codeforces import Codeforces


@shared_task
def check_topic_and_task():
    data = Codeforces()
    data.task_parser()
    data.writing_topics_to_database()
    data.writing_tasks_to_database()
    print(f'База обновлена!')
