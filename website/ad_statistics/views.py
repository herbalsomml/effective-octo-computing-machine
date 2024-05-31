from ad.models import MiniAd, Studio
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import MiniAdStatistic, StudioStatistic


@method_decorator(csrf_exempt, name='dispatch')
class TrackTelegramClick(View):
    def post(self, request, *args, **kwargs):
        slug = request.POST.get('slug')
        studio = get_object_or_404(Studio, slug=slug)
        obj, created = StudioStatistic.objects.get_or_create(
            defaults={"studio": studio, "date": timezone.now()},
            date=timezone.now(), studio=studio
        )
        obj.telegram_clicks += 1
        obj.save(update_fields=['telegram_clicks'])
        return JsonResponse(
            {
                'status': 'success',
            }
        )


@method_decorator(csrf_exempt, name='dispatch')
class TrackWebsiteClick(View):
    def post(self, request, *args, **kwargs):
        slug = request.POST.get('slug')
        studio = get_object_or_404(Studio, slug=slug)
        obj, created = StudioStatistic.objects.get_or_create(
            defaults={"studio": studio, "date": timezone.now()},
            date=timezone.now(), studio=studio
        )
        obj.website_clicks += 1
        obj.save(update_fields=['website_clicks'])
        return JsonResponse(
            {
                'status': 'success',
            }
        )


@method_decorator(csrf_exempt, name='dispatch')
class TrackPhoneClicks(View):
    def post(self, request, *args, **kwargs):
        slug = request.POST.get('slug')
        studio = get_object_or_404(Studio, slug=slug)
        obj, created = StudioStatistic.objects.get_or_create(
            defaults={"studio": studio, "date": timezone.now()},
            date=timezone.now(), studio=studio
        )
        obj.phone_clicks += 1
        obj.save(update_fields=['phone_clicks'])
        return JsonResponse(
            {
                'status': 'success',
            }
        )


@method_decorator(csrf_exempt, name='dispatch')
class TrackMiniAdClick(View):
    def post(self, request, *args, **kwargs):
        id = request.POST.get('id')
        mini_ad = get_object_or_404(MiniAd, id=id)
        obj, created = MiniAdStatistic.objects.get_or_create(
            defaults={"mini_ad": mini_ad, "date": timezone.now()},
            date=timezone.now(), mini_ad=mini_ad
        )
        obj.clicks += 1
        obj.save(update_fields=['clicks'])
        return JsonResponse(
            {
                'status': 'success',
            }
        )
