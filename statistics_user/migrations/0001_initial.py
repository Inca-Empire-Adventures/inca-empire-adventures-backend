# Generated by Django 4.1.1 on 2023-05-28 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StatisticsUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strength', models.IntegerField()),
                ('intelligence', models.IntegerField()),
                ('dexterity', models.IntegerField()),
                ('charisma', models.IntegerField()),
                ('wisdom', models.IntegerField()),
                ('constitucion', models.IntegerField()),
                ('ethnicityType', models.CharField(choices=[('Dios del Sol', 'Dios del Sol'), ('Dios de la Muerte', 'Dios de la Muerte'), ('Dios de la Luna', 'Dios de la Luna'), ('Dios de la Tierra', 'Dios de la Tierra')], max_length=50)),
            ],
        ),
    ]
