# Generated by Django 4.1.1 on 2023-01-22 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('damage', models.IntegerField()),
                ('character', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='characters.character')),
            ],
        ),
    ]
