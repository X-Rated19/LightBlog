# Generated by Django 3.2 on 2021-12-03 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_auto_20211129_1946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]