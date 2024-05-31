# Generated by Django 4.2.13 on 2024-05-31 10:54

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudioStatistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='Дата')),
                ('views', models.IntegerField(default=0, verbose_name='Просмотры')),
                ('telegram_clicks', models.IntegerField(default=0, verbose_name='Нажатий на Telegram')),
                ('studio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ad.studio')),
            ],
            options={
                'db_table': 'StudioStatistic',
            },
        ),
    ]
