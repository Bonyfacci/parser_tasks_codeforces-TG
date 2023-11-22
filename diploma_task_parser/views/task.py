from rest_framework import generics

from diploma_task_parser.models import Task
from diploma_task_parser.serializers.task import TaskSerializer


class TaskListAPIView(generics.ListAPIView):
    """
    Контроллер/Endpoint просмотра всех задач по определённой теме
    """

    serializer_class = TaskSerializer

    def get_queryset(self,):
        return Task.objects.filter(category=self.kwargs.get('pk'))


class TaskCreateAPIView(generics.CreateAPIView):
    """
    Контроллер/Endpoint создания задачи
    """

    serializer_class = TaskSerializer


class TaskRetrieveAPIView(generics.RetrieveAPIView):
    """
    Контроллер/Endpoint просмотра задачи
    """

    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskUpdateAPIView(generics.UpdateAPIView):
    """
    Контроллер/Endpoint редактирования задачи
    """

    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskDeleteAPIView(generics.DestroyAPIView):
    """
    Контроллер/Endpoint удаления задачи
    """

    queryset = Task.objects.all()
