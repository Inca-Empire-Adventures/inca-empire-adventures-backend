# Generated by Django 4.1.1 on 2023-04-14 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adventures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('character', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='characters.character')),
            ],
        ),
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('system', 'system'), ('assistant', 'assistant'), ('user', 'user')], max_length=50)),
                ('content', models.TextField()),
                ('adventure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adventures.adventures')),
            ],
        ),
    ]
