from rest_framework import serializers
from course.models import Payment
from course.validators import PayValidator


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
        validators = [PayValidator(field1='paid_course', field2='paid_lesson')]