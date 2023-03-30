# Generated by Django 4.1.1 on 2023-03-29 06:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('characters', '0001_initial'),
        ('statistics_user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='statisctic',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='statistics_user.statisticsuser'),
        ),
        migrations.AddField(
            model_name='character',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
