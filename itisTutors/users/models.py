from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils.datetime_safe import date

class course(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    num = models.IntegerField('Course Number')
    title = models.CharField('Course', max_length=31)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Profile(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField( upload_to='profile_pics',null=True)
    course = models.ForeignKey(course, verbose_name='Course' ,on_delete=models.CASCADE, default='')
    tutorPermissions = models.BooleanField('Права тьютора', default=False)
    initiative = models.BooleanField('Инициатива', default=False)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)