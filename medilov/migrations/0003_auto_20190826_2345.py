# Generated by Django 2.2.4 on 2019-08-26 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medilov', '0002_auto_20190821_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutunit',
            name='short_description',
            field=models.CharField(blank=True, max_length=350, verbose_name='short post description'),
        ),
        migrations.AlterField(
            model_name='aboutunit',
            name='title',
            field=models.CharField(max_length=30, verbose_name='img title'),
        ),
    ]
