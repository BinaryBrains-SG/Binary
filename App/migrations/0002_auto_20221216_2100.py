# Generated by Django 2.2.28 on 2022-12-16 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doubt',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.TextField(default=None)),
                ('answers', models.TextField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('pswd', models.CharField(max_length=20)),
                ('is_live', models.BooleanField(default=False)),
                ('img', models.ImageField(default=None, upload_to='Instructor/')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(default=None, max_length=254)),
                ('pswd', models.CharField(max_length=20)),
                ('img', models.ImageField(default=None, upload_to='Students/')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.TextField(default=None)),
                ('img', models.ImageField(default=None, upload_to='videos/')),
                ('url', models.URLField(default=None)),
            ],
        ),
        migrations.AlterField(
            model_name='course',
            name='img',
            field=models.ImageField(upload_to='Courses/'),
        ),
        migrations.AlterField(
            model_name='course',
            name='instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Instructor'),
        ),
        migrations.DeleteModel(
            name='Instructror',
        ),
        migrations.AddField(
            model_name='video',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Course'),
        ),
        migrations.AddField(
            model_name='student',
            name='Courses',
            field=models.ManyToManyField(to='App.Course'),
        ),
        migrations.AddField(
            model_name='student',
            name='instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Instructor'),
        ),
    ]
