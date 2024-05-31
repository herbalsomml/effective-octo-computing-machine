from django.urls import path

from .views import (TrackMiniAdClick, TrackPhoneClicks, TrackTelegramClick,
                    TrackWebsiteClick)

app_name = 'ad_statistics'

urlpatterns = [
    # другие маршруты
    path('track-telegram-click/',
         TrackTelegramClick.as_view(),
         name='telegram_click'),
    path('track-website-click/',
         TrackWebsiteClick.as_view(),
         name='website_click'),
    path('track-phone-click/',
         TrackPhoneClicks.as_view(),
         name='phone_click'),
    path('track-miniad-click/',
         TrackMiniAdClick.as_view(),
         name='miniad_click'),
]
