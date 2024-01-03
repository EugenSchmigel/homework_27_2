from django.db import models

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

