# Generated by Django 4.2.13 on 2024-05-31 12:28

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0001_initial'),
        ('ad_statistics', '0002_alter_studiostatistic_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MiniAdStatistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='Дата')),
                ('views', models.IntegerField(default=0, verbose_name='Просмотры')),
                ('clicks', models.IntegerField(default=0, verbose_name='Нажатий на рекламу')),
                ('mini_ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ad.miniad')),
            ],
            options={
                'verbose_name': 'Статистика мини рекламы',
                'verbose_name_plural': 'Статистика мини рекламы',
                'db_table': 'MiniAdStatistic',
            },
        ),
    ]
