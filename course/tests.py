import json

from rest_framework import status
from rest_framework.reverse import reverse
from  rest_framework.test import APITestCase

from course.models import Course, Lesson, Subscription
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        self.course = Course.objects.create(
            name='test'
        )
        self.lesson = Lesson.objects.create(
            name='test',
            course=self.course
        )

    def test_get_lesson_list(self):
        """ test lesson list """
        response = self.client.get(
            reverse('lesson_list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "name": self.lesson.name,
                        "course": self.lesson.course.id,
                        "id": self.lesson.id,
                        "foto": None,
                        "video": None,
                        "author": None
                    }
                ]
            }
        )

    def test_lesson_create(self):
        """ test create lesson """

        data = {
                "name": "TEst Lesson",
                "course": self.lesson.course.id
                }
        response = self.client.post(
            reverse('lesson_create'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            Lesson.objects.all().count(),
            2
        )

    # def test_lesson_delete(self):
    #     """ test lesson delete """
    #
    #     response = self.client.delete(
    #         '/lesson/2/delete/'
    #     )
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


    def test_lesson_update(self):
        """ test update lesson """

        course = Course.objects.create(
            name='Тестовый курс'
        )

        lesson = Lesson.objects.create(
            name='Тестовый урок',
            course=course
        )

        data = {
            'name': 'Test lesson update'
        }

        response = self.client.patch(
            f'/lesson/{lesson.id}/update/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json()['name'],
            'Test lesson update'
        )

    def test_retrieve_lesson(self):
        """Тестирование вывода одного урока"""

        course = Course.objects.create(
            name='Тестовый курс'
            )
        lesson = Lesson.objects.create(
            name='Тестовый урок',
            course=course
            )

        response = self.client.get(
            f'/lesson/{lesson.id}/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )


class SubscriptionTestCase(APITestCase):
    """ Тесты на создание и удаление подписки"""

    def setUp(self) -> None:
        self.course = Course.objects.create(
            name='test1'
        )

        self.user = User.objects.create(
            email='admin@arsolex.de',
            is_staff=True,
            is_active=True,
            is_superuser=False,
            first_name='Test',
            last_name='Admin'
        )

    def test_create_subscription(self):
        """ test create Subscription """
        data = {
                'user': self.user.pk,
                'course': self.course.pk
                }
        response = self.client.post(
            reverse('subscription_create'),
            data=data
        )

    def test_delete_subscribe(self):
        data = {
            'user': self.user.pk,
            'course': self.course.pk
        }
        response = self.client.post(
            reverse('subscription_create'),
            data=data
        )
        print(response.json())
        response = self.client.delete(
            '/subscription_create/1/'
        )