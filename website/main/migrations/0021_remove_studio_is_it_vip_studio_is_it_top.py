# Generated by Django 4.2.13 on 2024-05-25 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_studio_contact_button_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studio',
            name='is_it_vip',
        ),
        migrations.AddField(
            model_name='studio',
            name='is_it_top',
            field=models.BooleanField(default=False, verbose_name='Это TOP размещение?'),
        ),
    ]