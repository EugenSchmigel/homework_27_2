from rest_framework import serializers

from course.models import Course, Subscription
from course.serializers.lesson import LessonCourseSerializer

class CourseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('name', 'description',)


class CourseSerializer(serializers.ModelSerializer):

    lesson_count = serializers.IntegerField(source='lesson_set.all.count', read_only=True)
    lessons = LessonCourseSerializer(source='lesson_set', read_only=True, many=True)

    course_subscription = serializers.SerializerMethodField()

    def get_course_subscription(self, obj):
        return Subscription.objects.filter(course_subscription=obj, user=self.context['request'].user).exists()

    def get_lesson_count(self, instance):
        return instance.lesson_set.count()

    def get_lesson_count(self, instance):
        return instance.lesson_set.count()

    class Meta:
        model = Course
        fields = ('pk', 'title_course', 'image_course', 'description_course', 'lesson_count', 'lessons',
                  'course_subscription',)
    class Meta:
        model = Course
        fields = "__all__"