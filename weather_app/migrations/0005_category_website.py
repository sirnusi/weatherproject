# Generated by Django 3.2.7 on 2021-12-09 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather_app', '0004_remove_category_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='website',
            field=models.URLField(default=None),
        ),
    ]
