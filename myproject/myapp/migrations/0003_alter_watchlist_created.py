# Generated by Django 4.1 on 2022-09-10 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_platform_watchlist_delete_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]