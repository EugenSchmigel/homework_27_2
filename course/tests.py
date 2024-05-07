from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from course.models import Course, Lesson, Subscription
from users.models import User


class LessonApiTestCase(APITestCase):

    def setUp(self) -> None:
        user = User.objects.create(email='test@test.test', is_active=True)
        user.set_password('test_password')
        user.save()
        response = self.client.post(
            '/users/api/token/', data={"email": "admin@arsolex.de", "password": "12345"})
        self.token = response.json()["access"]

        self.user = user

    def test_create_lesson(self):

        heard = {
            "Authorization": f"Bearer {self.token}"
        }
        course = Course.objects.create(
            title_course='Тестовый курс',
            description_course='Тест'
        )

        data = {
            "name": "Test",
            "description": "Test",
            "course": course.id
        }

        response = self.client.post(
            '/course/lesson_create/create/',
            data=data,
            headers=heard
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertTrue(Course.objects.all().exists())

    def test_list_lesson(self):

        course = Course.objects.create(
            name='Тестовый курс',
            description='Тест',
        )

        lesson = Lesson.objects.create(
            name='Тестовый урок',
        )

        heard = {
            "Authorization": f"Bearer {self.token}"
        }

        response = self.client.get(
            '/course/lesson_list/',
            headers=heard
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_retrieve_lesson(self):

        course = Course.objects.create(
            name='Тестовый курс',
            description='Тест',
        )
        lesson = Lesson.objects.create(
            name='Тестовый урок',
        )
        heard = {
            "Authorization": f"Bearer {self.token}"
        }

        response = self.client.get(
            f'/course/lesson_retrieve/{lesson.id}/',
            headers=heard
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_lesson(self):

        course = Course.objects.create(
            name='Тестовый курс',
            description='Тест',
        )
        lesson = Lesson.objects.create(
            name='Тестовый урок',
        )

        heard = {
            "Authorization": f"Bearer {self.token}"
        }
        data = {
            'title_lesson': 'Test lesson update'
        }

        response = self.client.patch(
            f'/course/lesson_update/{lesson.id}/',
            data=data,
            headers=heard
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json()['title_lesson'],
            'Test lesson update'
        )

    def test_delete_lesson(self):


        course = Course.objects.create(
            name='Тестовый курс',
            description='Тест',
        )
        lesson = Lesson.objects.create(
            name='Тестовый урок',
        )
        heard = {
            "Authorization": f"Bearer {self.token}"
        }

        response = self.client.delete(
            f'/course/lesson_destroy/{lesson.id}/',
            headers=heard
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


class SubscriptionTestCase(APITestCase):

    def setUp(self) -> None:
        user = User.objects.create(email='test@test.test', is_active=True)
        user.set_password('test_password')
        user.save()
        response = self.client.post(
            '/users/api/token/', data={"email": "admin@arsolex.de", "password": "12345"})
        self.token = response.json()["access"]

        self.user = user

    def test_create_subscription(self):

        heard = {
            "Authorization": f"Bearer {self.token}"
        }
        course = Course.objects.create(
            title_course='Тестовый курс',
            description_course='Тест',
        )
        data = {
            'course_subscription': course.id,
        }
        response = self.client.post(
            '/course/subscription_create/',
            data=data,
            headers=heard
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_delete_subscription(self):

        heard = {
            "Authorization": f"Bearer {self.token}"
        }
        course = Course.objects.create(
            name='Тестовый курс',
            description='Тест',
        )
        subscription = Subscription.objects.create(
            user=self.user,
            course_subscription=course
        )
        response = self.client.delete(
            f'/course/subscription_destroy/{subscription.id}/',
            headers=heard
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )