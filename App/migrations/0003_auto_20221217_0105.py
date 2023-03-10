# Generated by Django 2.2.28 on 2022-12-16 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_auto_20221216_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='levels',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(default=None, max_length=254, unique=True),
        ),
    ]
