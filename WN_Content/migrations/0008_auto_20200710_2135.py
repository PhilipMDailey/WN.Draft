# Generated by Django 3.0 on 2020-07-10 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WN_Content', '0007_auto_20200710_2107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='video',
        ),
        migrations.AddField(
            model_name='post',
            name='Podcast',
            field=models.CharField(max_length=300, null=True),
        ),
    ]