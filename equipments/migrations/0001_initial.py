# Generated by Django 4.1.1 on 2022-10-27 02:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('character', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='characters.character')),
            ],
        ),
    ]
