# Generated by Django 3.1.7 on 2021-03-14 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='url_ref',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='tweeprint',
            name='url_ref',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
    ]