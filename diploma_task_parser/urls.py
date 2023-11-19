from django.urls import path

from diploma_task_parser.apps import DiplomaTaskParserConfig
from diploma_task_parser.views import home

app_name = DiplomaTaskParserConfig.name

urlpatterns = [
    path('', home, name='home'),  # http://127.0.0.1:8000/task_parser/
]
