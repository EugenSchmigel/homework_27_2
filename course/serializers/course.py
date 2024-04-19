from rest_framework import serializers

from course.models import Course
from course.serializers.lesson import LessonCourseSerializer

class CourseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('name', 'description',)


class CourseSerializer(serializers.ModelSerializer):

    lesson_count = serializers.IntegerField(source='lesson_set.all.count', read_only=True)  # вывод количества уроков
    lessons = LessonCourseSerializer(source='lesson_set', read_only=True, many=True)  # вывод уроков

    def get_lesson_count(self, instance):
        return instance.lesson_set.count()

    class Meta:
        model = Course
        fields = "__all__"