# Generated by Django 4.1 on 2022-09-16 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=models.SlugField(default='slug', null=True),
        ),
    ]