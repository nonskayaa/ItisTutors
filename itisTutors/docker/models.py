from django.db import models
from tutors.models import Subject
from users.models import Course
# Create your models here.

class DockerPost(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    discipline = models.ForeignKey(Subject,related_name='DockerPosts',on_delete=models.CASCADE, default='', null=False)
    title=models.CharField('Заголовок',default='Заголовок',max_length=511,null=False)
    postText = models.TextField('Текст поста в хранилище', default='Тут пока нет никаких ссылок')
    course = models.ForeignKey(Course,related_name='DockerPosts', verbose_name='Course' ,on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.discipline.title+' '+self.course.title

    class Meta:
        verbose_name = 'Пост в Хранилище'
        verbose_name_plural = 'Посты в Хранилище'