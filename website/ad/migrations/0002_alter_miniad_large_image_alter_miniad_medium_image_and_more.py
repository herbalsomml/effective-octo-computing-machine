# Generated by Django 4.2.13 on 2024-06-11 13:12

import cloudflare_images.field
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miniad',
            name='large_image',
            field=cloudflare_images.field.CloudflareImagesField(upload_to='', variant='public', verbose_name='Изображение для больших устройств'),
        ),
        migrations.AlterField(
            model_name='miniad',
            name='medium_image',
            field=cloudflare_images.field.CloudflareImagesField(upload_to='', variant='public', verbose_name='Изображение для средних устройств'),
        ),
        migrations.AlterField(
            model_name='miniad',
            name='small_image',
            field=cloudflare_images.field.CloudflareImagesField(upload_to='', variant='public', verbose_name='Изображение для маленьких устройств'),
        ),
        migrations.AlterField(
            model_name='studio',
            name='image',
            field=cloudflare_images.field.CloudflareImagesField(upload_to='', variant='public', verbose_name='Изображение'),
        ),
    ]
