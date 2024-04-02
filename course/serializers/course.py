from rest_framework import serializers

from course.models import Course
from course.serializers.lesson import LessonCourseSerializer


class CourseSerializer(serializers.ModelSerializer):

    lesson_count = serializers.IntegerField(source='lesson_set.all.count', read_only=True)  # вывод количества уроков
    lessons = LessonCourseSerializer(source='lesson_set', read_only=True, many=True)  # вывод уроков

    class Meta:
        model = Course
        fields = "__all__"