# Generated by Django 5.0.6 on 2024-06-21 18:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('university_name', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=50)),
                ('batch', models.CharField(max_length=50)),
                ('roll', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(default='01', max_length=100)),
                ('student_img', models.ImageField(upload_to='student/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
