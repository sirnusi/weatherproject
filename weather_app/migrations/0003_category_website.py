# Generated by Django 3.2.7 on 2021-12-09 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather_app', '0002_auto_20211209_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='website',
            field=models.URLField(default=None),
            preserve_default=False,
        ),
    ]
