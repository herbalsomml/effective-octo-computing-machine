from django.contrib import admin

from .models import MiniAdStatistic, StudioStatistic


class StudioStatisticAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'date',
        'views',
        'telegram_clicks',
        'website_clicks',
        'phone_clicks'
    )
    search_fields = (
        '__str__',
    )


class MiniAdStatisticAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'date',
        'views',
        'clicks'
    )
    search_fields = (
        '__str__',
    )


admin.site.register(StudioStatistic, StudioStatisticAdmin)
admin.site.register(MiniAdStatistic, MiniAdStatisticAdmin)
