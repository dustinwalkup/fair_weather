# Generated by Django 3.1.1 on 2020-09-05 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_remove_todo_new_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='temp',
            field=models.IntegerField(default=58),
        ),
        migrations.AddField(
            model_name='todo',
            name='zip',
            field=models.IntegerField(default=0),
        ),
    ]