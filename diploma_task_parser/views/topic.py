from django.shortcuts import render
from django.views.generic import ListView
from rest_framework import viewsets

from diploma_task_parser.models import Topic
from diploma_task_parser.serializers.topic import TopicSerializer


class TopicViewSet(viewsets.ModelViewSet):
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()


class TopicListView(ListView):
    model = Topic
    template_name = 'topic_list.html'
