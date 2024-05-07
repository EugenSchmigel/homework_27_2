from rest_framework import serializers
from course.models import Lesson
from course.validators import UrlValidator


class LessonCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('pk', 'name',)


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [UrlValidator(field='url_lesson')]