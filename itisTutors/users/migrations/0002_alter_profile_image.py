# Generated by Django 4.2 on 2023-06-02 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.png', null=True, upload_to='users/static/users/profile_pics'),
        ),
    ]
