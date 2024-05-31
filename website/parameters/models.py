from django.db import models


class BaseParameter(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class City(BaseParameter):
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class ExperienceChoices(BaseParameter):
    class Meta:
        verbose_name = 'Опыт работы'
        verbose_name_plural = 'Опыт работы'


class FormatChoices(BaseParameter):
    class Meta:
        verbose_name = 'Тип студии'
        verbose_name_plural = 'Типы студий'


class GenderChoices(BaseParameter):
    class Meta:
        verbose_name = 'Гендер'
        verbose_name_plural = 'гендеры'


class PayoutsChoices(BaseParameter):
    class Meta:
        verbose_name = 'Выплата'
        verbose_name_plural = 'выплаты'


class ShiftsChoices(BaseParameter):
    class Meta:
        verbose_name = 'Смена'
        verbose_name_plural = 'смены'
