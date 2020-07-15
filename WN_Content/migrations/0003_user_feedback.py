# Generated by Django 3.0 on 2020-06-25 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WN_Content', '0002_auto_20200612_0013'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('feedback', models.TextField()),
                ('related_resource', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='WN_Content.Resource')),
            ],
        ),
    ]