from rest_framework import serializers

from diploma_task_parser.models import Topic


class TopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = '__all__'
