# Generated by Django 4.2.13 on 2024-05-31 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad_statistics', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studiostatistic',
            options={'verbose_name': 'Статистика студий', 'verbose_name_plural': 'Статистика студий'},
        ),
        migrations.AddField(
            model_name='studiostatistic',
            name='phone_clicks',
            field=models.IntegerField(default=0, verbose_name='Нажатий на телефон'),
        ),
        migrations.AddField(
            model_name='studiostatistic',
            name='website_clicks',
            field=models.IntegerField(default=0, verbose_name='Нажатий на вебсайт'),
        ),
    ]
