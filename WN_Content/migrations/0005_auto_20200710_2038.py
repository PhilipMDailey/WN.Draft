# Generated by Django 3.0 on 2020-07-10 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WN_Content', '0004_delete_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Video_Url',
            field=models.URLField(verbose_name=''),
        ),
    ]
