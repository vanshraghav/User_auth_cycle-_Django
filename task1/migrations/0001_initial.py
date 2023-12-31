# Generated by Django 4.1.7 on 2023-06-25 11:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Draft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.TextField(default='draft')),
                ('title', models.TextField(default='Hi')),
                ('content1', models.TextField(default='Hi')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('category', models.TextField(default='Hi')),
                ('summary', models.TextField(default='Hi')),
                ('img', models.ImageField(upload_to='pics')),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of', models.TextField(default='Hi')),
                ('first_name', models.TextField(default='Hi')),
                ('last_name', models.TextField(default='Hi')),
                ('prof_pic', models.ImageField(upload_to='pics')),
                ('username', models.TextField(default='Hi')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.TextField(default='Hi')),
                ('address', models.TextField(default='Hi')),
                ('city', models.TextField(default='Hi')),
                ('state', models.TextField(default='Hi')),
                ('pincode', models.TextField(default='Hi')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='Hi')),
                ('content1', models.TextField(default='Hi')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('category', models.TextField(default='Hi')),
                ('summary', models.TextField(default='Hi')),
                ('img', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
