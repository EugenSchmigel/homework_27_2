from rest_framework import serializers

from course.models import Lesson


class LessonCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('pk', 'name',)


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"