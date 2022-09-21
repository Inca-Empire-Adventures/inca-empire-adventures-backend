# Generated by Django 3.2.15 on 2022-09-18 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameGroup', models.CharField(max_length=25)),
                ('namePlayer', models.CharField(max_length=25)),
                ('raceId', models.IntegerField()),
                ('professionId', models.IntegerField()),
            ],
        ),
    ]
