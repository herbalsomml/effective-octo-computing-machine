from ad.models import MiniAd, Studio
from django.db import models
from django.utils import timezone


class StudioStatistic(models.Model):
    class Meta:
        verbose_name = 'Статистика студий'
        verbose_name_plural = 'Статистика студий'
        db_table = "StudioStatistic"

    studio = models.ForeignKey(Studio, on_delete=models.CASCADE)
    date = models.DateField('Дата', default=timezone.now)
    views = models.IntegerField('Просмотры', default=0)
    telegram_clicks = models.IntegerField('Нажатий на Telegram', default=0)
    website_clicks = models.IntegerField('Нажатий на вебсайт', default=0)
    phone_clicks = models.IntegerField('Нажатий на телефон', default=0)

    def __str__(self):
        return self.studio.name


class MiniAdStatistic(models.Model):
    class Meta:
        verbose_name = 'Статистика мини рекламы'
        verbose_name_plural = 'Статистика мини рекламы'
        db_table = "MiniAdStatistic"

    mini_ad = models.ForeignKey(MiniAd, on_delete=models.CASCADE)
    date = models.DateField('Дата', default=timezone.now)
    views = models.IntegerField('Просмотры', default=0)
    clicks = models.IntegerField('Нажатий на рекламу', default=0)

    def __str__(self):
        return self.mini_ad.name
