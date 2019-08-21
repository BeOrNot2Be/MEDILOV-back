# Generated by Django 2.2.4 on 2019-08-20 23:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True, verbose_name='gallery title')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='gallery description')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='last update')),
                ('gallery_logo', models.CharField(max_length=1000, verbose_name='img logo url')),
            ],
            options={
                'verbose_name': 'gallery',
                'verbose_name_plural': 'galleris',
            },
        ),
        migrations.CreateModel(
            name='GalleryTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True, verbose_name='topic title')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='last update')),
            ],
            options={
                'verbose_name': 'gallery topic',
                'verbose_name_plural': 'gallery topics',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='service title')),
                ('short_description', models.CharField(blank=True, max_length=350, verbose_name='short service description')),
                ('long_description', models.CharField(max_length=5000, verbose_name='long service description')),
                ('img_name', models.CharField(blank=True, max_length=30, verbose_name='img name')),
                ('url', models.CharField(blank=True, max_length=1000, verbose_name='img url')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='last update')),
            ],
            options={
                'verbose_name': 'service',
                'verbose_name_plural': 'services',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='img title')),
                ('url', models.CharField(max_length=1000, unique=True, verbose_name='img url')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='last update')),
                ('gallery', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='photos', to='medilov.Gallery')),
            ],
            options={
                'verbose_name': 'photo',
                'verbose_name_plural': 'photos',
            },
        ),
        migrations.AddField(
            model_name='gallery',
            name='topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='galleries', to='medilov.GalleryTopic'),
        ),
        migrations.CreateModel(
            name='AboutUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='service title')),
                ('short_description', models.CharField(blank=True, max_length=350, verbose_name='short service description')),
                ('phrase', models.CharField(blank=True, max_length=10, verbose_name='letters for phrase')),
                ('url', models.CharField(blank=True, max_length=1000, verbose_name='img url')),
                ('date', models.DateField()),
                ('color', models.CharField(blank=True, max_length=7)),
                ('parent', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='medilov.AboutUnit')),
            ],
            options={
                'verbose_name': 'about post',
                'verbose_name_plural': 'about posts',
            },
        ),
    ]
