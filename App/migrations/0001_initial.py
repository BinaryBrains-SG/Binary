# Generated by Django 2.2.28 on 2022-12-16 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instructror',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('pswd', models.TextField(max_length=20)),
                ('is_live', models.BooleanField(default=False)),
                ('img', models.ImageField(upload_to='media/instructor/')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('img', models.ImageField(upload_to='media/courses/')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Instructror')),
            ],
        ),
    ]
