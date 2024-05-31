from django.urls import include, path

from . import views

app_name = 'ad'

urlpatterns = [path('',
                    views.StudioListView.as_view(),
                    name='index'),
               path('search/',
                    views.StudioSearchList.as_view(),
                    name='studio_search'),
               path('studio/<slug:slug>/',
                    views.StudioView.as_view(),
                    name='studio_view'),]
