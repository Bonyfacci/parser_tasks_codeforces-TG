from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from diploma_task_parser.models import Topic, Task


class TopicTestCase(APITestCase):
    """
    Для тестирования тем (Topic)
    """

    def setUp(self):
        self.topic = Topic.objects.create(
            name='TestTopic',
        )

    def test_get_topic(self):
        """
        Тест TopicListView
        """
        response = self.client.get(
            reverse('diploma_task_parser:topic_list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            Topic.objects.all().count(),
            1
        )

        self.assertContains(
            response,
            'TestTopic'
        )


class TaskTestCase(APITestCase):
    """
    Для тестирования задач (Task)
    """

    def setUp(self):
        self.topic = Topic.objects.create(
            name='TestTopic',
        )

        self.task = Task.objects.create(
            contest_id=1000,
            contest_index='A',
            name='TestTask',
            type='PROGRAMMING',
            points=555,
            rating=888,
            solved_count=15,
        )

        self.task.category.set(
            [self.topic.id]
        )

    def test_get_task(self):
        """
        Тест TaskListAPIView
        """

        response = self.client.get(
            reverse(
                'diploma_task_parser:tasks_list',
                args=[self.topic.id]
            )
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertContains(
            response,
            'TestTask'
        )

    def test_post_task(self):
        """
        Тест TaskCreateAPIView
        """

        self.new_task = {
            'contest_id': 1001,
            'contest_index': 'B',
            'name': 'NewTask',
            'type': 'PROGRAMMING',
            'points': 666,
            'rating': 999,
            'solved_count': 16,
            'category': [self.topic.id]
        }

        response = self.client.post(
            reverse('diploma_task_parser:task_create'),
            self.new_task
        )

        # print(response.content.decode('utf-8'))

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )  # Ожидаемый код ответа для успешного создания

    def test_retrieve_task(self):
        """
        Тест TaskRetrieveAPIView
        """

        response = self.client.get(
            reverse('diploma_task_parser:task_detail',
                    args=[self.task.id])
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertContains(
            response,
            'TestTask'
        )

    def test_patch_task(self):
        """
        Тест TaskUpdateAPIView
        """

        data = {
            'name': 'UpdatedTask'
        }

        response = self.client.patch(
            reverse(
                'diploma_task_parser:task_update',
                args=[self.task.id]
            ),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        # print(response.content.decode('utf-8'))

        self.task.refresh_from_db()

        self.assertEqual(
            self.task.name,
            'UpdatedTask'
        )

    def test_delete_task(self):
        """
        Тест TaskDeleteAPIView
        """

        response = self.client.delete(
            reverse(
                'diploma_task_parser:task_delete',
                args=[self.task.id]
            )
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )  # Ожидаемый код ответа для успешного удаления

        self.assertFalse(
            Task.objects.filter(name='TestTask').exists()
        )
