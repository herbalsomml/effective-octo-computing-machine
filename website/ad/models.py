from datetime import datetime, timedelta
from io import BytesIO

from django.core.exceptions import ValidationError
from cloudflare_images.field import CloudflareImagesField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone
from parameters.models import (City, ExperienceChoices, FormatChoices,
                               GenderChoices, PayoutsChoices, ShiftsChoices)


class Studio(models.Model):

    name = models.CharField(
        max_length=90,
        blank=False,
        verbose_name='Название cтудии'
    )

    slug = models.SlugField(
        max_length=128,
        blank=False
    )

    image = image = CloudflareImagesField(
        verbose_name='Изображение',
    )

    description = models.TextField(
        verbose_name='Полное описание'
    )

    telegram = models.CharField(
        verbose_name='Телеграм аккаунт',
        blank=True,
        max_length=128
    )

    website = models.URLField(
        verbose_name='Ссылка на сайт',
        blank=True,
        max_length=258
    )

    phone = models.CharField(
        verbose_name='Номер телефона',
        blank=True,
        max_length=40
    )

    cities = models.ManyToManyField(
        City,
        verbose_name='Города работы',
        blank=False
    )

    experience = models.ManyToManyField(
        ExperienceChoices,
        verbose_name='Опыт работы',
    )

    format = models.ManyToManyField(
        FormatChoices,
        verbose_name='Формат работы',
    )

    gender = models.ManyToManyField(
        GenderChoices,
        verbose_name='Гендер',
        blank=False
    )

    english = models.BooleanField(
        default=False,
        verbose_name='Требуется ли знание английского'
    )

    min_age = models.IntegerField(
        default=18,
        verbose_name='Минимальный возраст модели',
        validators=[
            MinValueValidator(18),
            MaxValueValidator(85)
        ],
    )

    max_age = models.IntegerField(
        default=60,
        verbose_name='Максильмальный возраст модели',
        validators=[
            MinValueValidator(18),
            MaxValueValidator(85)
        ],
    )

    payouts = models.ManyToManyField(
        PayoutsChoices,
        verbose_name='Выплаты',
    )

    min_percent = models.IntegerField(
        default=50,
        verbose_name='Минимальный процент выплаты модели',
        validators=[
            MinValueValidator(10),
            MaxValueValidator(100)
        ],
    )

    max_percent = models.IntegerField(
        default=90,
        verbose_name='Максимальный процент выплаты модели',
        validators=[
            MinValueValidator(10),
            MaxValueValidator(100)
        ],
    )

    shifts = models.ManyToManyField(
        ShiftsChoices,
        verbose_name='Смены',
    )

    operator = models.BooleanField(
        default=False,
        verbose_name='Наличие оператора',
    )

    is_it_premium = models.BooleanField(
        default=False,
        verbose_name='Это премиум размещение?'
    )

    contact_button_icon = models.CharField(
        default='fa-solid fa-message',
        verbose_name='Иконка кнопки связаться для премиума',
        max_length=128,
        blank=True
    )

    contact_button_text = models.CharField(
        default='Связаться',
        verbose_name='Текст кнопки связи для премиума',
        max_length=256,
        blank=True
    )

    contact_button_link = models.CharField(
        default='#',
        max_length=128,
        verbose_name='Ссылка для кнопки связаться премиума',
        blank=True
    )

    is_it_top = models.BooleanField(
        default=False,
        verbose_name='Это TOP размещение?'
    )

    when_it_ends = models.DateTimeField(
        default=None,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Студия'
        verbose_name_plural = 'студии'
        db_table = 'studio'

    def __str__(self):
        return f'{self.name}'

    def clean(self):
        super().clean()
        if self.min_age > self.max_age:
            raise ValidationError({
                'min_age': 'min_age не может быть больше max_age',
                'max_age': 'max_age не может быть меньше min_age'
            })

        if self.min_percent > self.max_percent:
            raise ValidationError({
                'min_percent': 'min_percent не может быть больше max_percent',
                'max_percent': 'max_percent не может быть меньше min_percent'
            })

    def save(self, *args, **kwargs):
        if self.when_it_ends is None:
            self.when_it_ends = timezone.now() + timedelta(days=30)
        super(Studio, self).save(*args, **kwargs)


class MiniAd(models.Model):
    name = models.CharField(
        blank=False,
        max_length=50,
        verbose_name='Название'
    )
    link = models.URLField(
        max_length=258,
        verbose_name='Ссылка'
    )
    small_image = CloudflareImagesField(
        verbose_name='Изображение для маленьких устройств',
    )
    medium_image = CloudflareImagesField(
        verbose_name='Изображение для средних устройств',
    )
    large_image = CloudflareImagesField(
        verbose_name='Изображение для больших устройств',
    )
    when_it_ends = models.DateTimeField(
        default=None,
        blank=True,
        null=True,
        verbose_name='До какого момента будет отображаться на сайте'
    )

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        if self.when_it_ends is None:
            self.when_it_ends = timezone.now() + timedelta(days=30)
        super(MiniAd, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Мини реклама'
        verbose_name_plural = 'Мини реклама'
