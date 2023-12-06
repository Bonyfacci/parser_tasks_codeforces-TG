from django.shortcuts import render
from rest_framework import generics

from diploma_task_parser.models import Task
from diploma_task_parser.paginators import TaskPaginator
from diploma_task_parser.serializers.task import TaskSerializer


class TaskListAPIView(generics.ListAPIView):
    """
    Контроллер/Endpoint просмотра всех задач по определённой теме
    """

    serializer_class = TaskSerializer
    pagination_class = TaskPaginator
    template_name = 'diploma_task_parser/task_list.html'

    def get_queryset(self,):
        return Task.objects.filter(category=self.kwargs.get('pk')).order_by("-solved_count")

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return render(request, self.template_name, {'object_list': serializer.data})


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
