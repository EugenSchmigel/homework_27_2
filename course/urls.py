from django.urls import path
from rest_framework import routers

from course.views.course import *
from course.views.lesson import *
from course.views.payment import *
from course.views.subscription import SubscriptionCreateAPIView, SubscriptionDestroyAPIView


urlpatterns = [
    path('', LessonListView.as_view(), name='lesson_list'),
    path('payment/', PaymentListView.as_view()),
    path('<int:pk>/', LessonDetailView.as_view()),
    path('<int:pk>/update/', LessonUpdateView.as_view()),
    path('create/', LessonCreateView.as_view(), name='lesson_create'),

    path('<int:pk>/delete/', LessonDeleteView.as_view()),

    path('subscription_create/', SubscriptionCreateAPIView.as_view(), name='subscription_create'),
    path('subscription_destroy/<int:pk>/', SubscriptionDestroyAPIView.as_view(), name='subscription_destroy'),
    path('payment_create/', PaymentCreateAPIView.as_view(), name='payment_create'),

]

router = routers.SimpleRouter()
router.register('course', CourseViewSet)

urlpatterns += router.urls
