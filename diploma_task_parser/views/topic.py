from rest_framework import viewsets

from diploma_task_parser.models import Topic
from diploma_task_parser.serializers.topic import TopicSerializer


class TopicViewSet(viewsets.ModelViewSet):
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()
