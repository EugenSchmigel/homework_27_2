from django.db import models
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='Poroda')
    description = models.TextField(**NULLABLE, verbose_name='Opisanie')
    foto = models.ImageField(upload_to='course/', **NULLABLE, verbose_name='Preview')


    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'


class Lesson(models.Model):
    name = models.CharField(max_length=250, verbose_name='Klichka')
    course = models.ForeignKey("course.Course", on_delete=models.CASCADE, verbose_name='Poroda')
    foto = models.ImageField(upload_to='course/', **NULLABLE, verbose_name='Preview')
    video = models.TextField(**NULLABLE, verbose_name='Url to video')

    def __str__(self):
        return f'{self.name} ({self.course})'

    class Meta:
        verbose_name = 'lesson'
        verbose_name_plural = 'lessons'


class Payment(models.Model):
    PAY_CARD = 'card'
    PAY_CASH = 'cash'

    PAY_TYPES = (
        (PAY_CASH, 'cash'),
        (PAY_CARD, 'card')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user', **NULLABLE)
    date_of_payment = models.DateField(verbose_name='date of payment', **NULLABLE, auto_now_add=True)
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='paid course', **NULLABLE)
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='paid lesson', **NULLABLE)
    amount_payment = models.PositiveIntegerField(verbose_name='amount of payment')
    method_payment = models.CharField(max_length=20, choices=PAY_TYPES, verbose_name='payment method')


    def __str__(self):
        return f'{self.paid_course if self.paid_course else self.paid_lesson} - {self.amount_payment}'

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'


class Subscription(models.Model):
    user = models.ForeignKey(User, verbose_name='user', on_delete=models.CASCADE, **NULLABLE)
    course_subscription = models.ForeignKey(Course, verbose_name='course subscription', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} - {self.course_subscription}'

    class Meta:
        verbose_name = 'Subscription'
        verbose_name_plural = 'Subscriptions'