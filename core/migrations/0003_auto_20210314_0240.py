# Generated by Django 3.1.7 on 2021-03-14 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210314_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweeprint',
            name='link',
            field=models.URLField(unique=True),
        ),
    ]
