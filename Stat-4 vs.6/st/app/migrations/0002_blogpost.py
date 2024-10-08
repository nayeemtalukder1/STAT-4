# Generated by Django 5.0.6 on 2024-06-21 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('content', models.TextField()),
                ('excerpt', models.TextField()),
                ('image', models.ImageField(upload_to='blog/')),
                ('published_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('published', 'Published'), ('pending', 'Pending')], default='pending', max_length=10)),
            ],
        ),
    ]
