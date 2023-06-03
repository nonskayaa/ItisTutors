from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile, Course

def create_profile(sender, instance, created, **kwargs):
    if created:
        course = Course.objects.first() # Выберите курс по умолчанию для нового профиля
        Profile.objects.create(user=instance, course=course)

post_save.connect(create_profile, sender=User)