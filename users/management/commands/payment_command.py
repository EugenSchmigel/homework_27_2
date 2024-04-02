from django.core.management import BaseCommand

from course.models import Payment


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        payment = Payment.objects.create(
            date_of_payment='2024-03-16',
            amount_payment=1500,
            method_payment='card'
        )

        payment.save()