# Generated by Django 3.0.6 on 2020-06-14 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0007_bookmark_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='comments',
            field=models.IntegerField(default=0),
        ),
    ]
