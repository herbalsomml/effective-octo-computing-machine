from django.contrib import admin
from django.contrib.auth.models import Group, User

from .models import (City, ExperienceChoices, FormatChoices, GenderChoices,
                     MiniAd, PayoutsChoices, ShiftsChoices, Studio)


@admin.register(Studio)
class StudioAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'telegram',
        'website',
        'phone'
    )
    list_filter = (
        'cities',
    )
    fieldsets = (
        ('Основное', {
            'fields': (
                'name',
                'slug',
                'image',
                'description',
                'cities',
                'when_it_ends'
            )
        }),
        ('Контактная информаиця', {
            'fields': (
                'telegram',
                'website',
                'phone'
            )
        }),
        ('Условия работы', {
            'fields': (
                'experience',
                'format',
                'gender',
                'english',
                'min_age',
                'max_age',
                'payouts',
                'min_percent',
                'max_percent',
                'shifts',
                'operator'
            )
        }),
        ('Премиум настройки', {
            'fields': (
                'is_it_premium',
                'contact_button_icon',
                'contact_button_text',
                'contact_button_link'
            )
        }),

        ('Топ настройки', {
            'fields': (
                'is_it_top',
            )
        }),
    )


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(MiniAd)
