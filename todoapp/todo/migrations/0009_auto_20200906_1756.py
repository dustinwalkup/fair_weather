# Generated by Django 3.1.1 on 2020-09-06 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0008_auto_20200906_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='zip',
            field=models.CharField(max_length=5),
        ),
    ]
