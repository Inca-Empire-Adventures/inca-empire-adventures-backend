# Generated by Django 4.1.1 on 2022-11-01 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('statistics_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('statistics', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='statistics_user.statisticsuser')),
            ],
        ),
    ]
