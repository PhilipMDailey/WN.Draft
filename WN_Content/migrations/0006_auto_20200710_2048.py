# Generated by Django 3.0 on 2020-07-10 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WN_Content', '0005_auto_20200710_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Video_Url',
            field=models.URLField(blank=True, null=True),
        ),
    ]