from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView

from course.models import Payment
from course.serializers.payment import PaymentSerializer


class PaymentListView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['paid_course', 'paid_lesson', 'method_payment']
    ordering_fields = ['date_of_payment']