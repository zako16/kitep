# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 11:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=50, null=True)),
                ('cover', models.ImageField(null=True, upload_to='books/covers')),
                ('description', models.TextField()),
                ('exchange', models.BooleanField(default=False)),
                ('sale', models.BooleanField(default=False)),
                ('price', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_issue', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='CoverTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Тип обложки',
                'verbose_name_plural': 'Типы обложек',
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Издательство',
                'verbose_name_plural': 'Издательства',
            },
        ),
        migrations.CreateModel(
            name='Statuses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Статус(Состояние) книги',
                'verbose_name_plural': 'Статусы книг',
            },
        ),
        migrations.CreateModel(
            name='Years',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Год выхода книги',
                'verbose_name_plural': 'Года',
            },
        ),
        migrations.AddField(
            model_name='books',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Categories'),
        ),
        migrations.AddField(
            model_name='books',
            name='coverType',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='books.CoverTypes'),
        ),
        migrations.AddField(
            model_name='books',
            name='publisher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='books.Publisher'),
        ),
        migrations.AddField(
            model_name='books',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='books.Statuses'),
        ),
        migrations.AddField(
            model_name='books',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='books',
            name='year',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='books.Years'),
        ),
    ]
