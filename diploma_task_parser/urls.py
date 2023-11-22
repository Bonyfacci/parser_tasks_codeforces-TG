from django.urls import path
from rest_framework.routers import DefaultRouter

from diploma_task_parser.apps import DiplomaTaskParserConfig
from diploma_task_parser.views.task import TaskListAPIView, TaskCreateAPIView, \
    TaskRetrieveAPIView, TaskUpdateAPIView, TaskDeleteAPIView
from diploma_task_parser.views.topic import TopicViewSet
from diploma_task_parser.views.views import home

app_name = DiplomaTaskParserConfig.name

router = DefaultRouter()
router.register(r'topic', TopicViewSet, basename='topic')

urlpatterns = [
    path('', home, name='home'),  # http://127.0.0.1:8000/task_parser/

    path('tasks/', TaskListAPIView.as_view(), name='tasks_list'),
    #                   http://127.0.0.1:8000/task_parser/tasks/

    path('task/create/', TaskCreateAPIView.as_view(), name='task_create'),
    #                   http://127.0.0.1:8000/task_parser/task/create/

    path('task/<int:pk>/', TaskRetrieveAPIView.as_view(), name='task_detail'),
    #                   http://127.0.0.1:8000/task_parser/task/<int:pk>/

    path('task/update/<int:pk>/', TaskUpdateAPIView.as_view(), name='task_update'),
    #                   http://127.0.0.1:8000/task_parser/task/update/<int:pk>/

    path('task/delete/<int:pk>/', TaskDeleteAPIView.as_view(), name='task_delete'),
    #                   http://127.0.0.1:8000/task_parser/task/delete/<int:pk>/
] + router.urls
