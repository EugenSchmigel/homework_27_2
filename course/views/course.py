from rest_framework.viewsets import ModelViewSet

from course.models import Course
from course.serializers.course import CourseSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def perform_create(self, serializer):
        serializer.save()
        self.request.user.course_set.add(serializer.instance)

    def get_queryset(self):
        if not self.request.user.is_staff:
            return Course.objects.filter(autor=self.request.user)
        elif self.request.user.is_staff:
            return Course.objects.all()

