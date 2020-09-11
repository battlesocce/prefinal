# Generated by Django 2.1.7 on 2020-09-04 07:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200904_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='team',
            name='teamname',
            field=models.CharField(blank=True, default='Team name 626', max_length=100, null=True),
        ),
    ]
