# Generated by Django 4.2 on 2023-06-02 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.png', null=True, upload_to='profile_pics'),
        ),
    ]