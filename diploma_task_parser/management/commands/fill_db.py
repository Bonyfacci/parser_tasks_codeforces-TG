from django.core.management import BaseCommand

from diploma_task_parser.services.codeforces import Codeforces


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        data = Codeforces()
        data.task_parser()
        data.writing_topics_to_database()
        data.writing_tasks_to_database()
