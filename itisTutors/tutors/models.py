from django.db import models
from django.contrib.auth.models import User
from users.models import Profile,Course
from django.urls import reverse
# Create your models here.


class Subject(models.Model):
    title=models.CharField('Предмет', max_length=127, default='Общие')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)#models.CharField('Course', max_length=15, default='1')
    #docker=models.ForeignKey(DockerPost, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Предмет'
        verbose_name_plural = 'Предметы'



class TutorInfo(models.Model):
    name = models.CharField('Имя', max_length=63)
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    discipline = models.ForeignKey(Subject,related_name='Tutors', on_delete=models.CASCADE, default='', null=True)
    contacts = models.TextField('Контакты')
    #user = models.ForeignKey(User, on_delete=models.CASCADE, default='', null=True)#related_name='Tutors'
    profile = models.ForeignKey(Profile,related_name='Tutors', on_delete=models.CASCADE, default='', null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('TutorDetail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name='Информация о Тьюторе'
        verbose_name_plural = 'Информация о Тьюторах'


