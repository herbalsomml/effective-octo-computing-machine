from itertools import chain

from ad_statistics.models import MiniAdStatistic, StudioStatistic
from constance import config
from django.db.models import BooleanField, Case, IntegerField, Value, When
from django.db.models.functions import Random
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views.generic import DetailView, ListView, View

from .forms import StudioSearchForm
from .models import MiniAd, Studio


class StudioView(View):
    template_name = 'main/studio.html'
    context_object_name = 'studio'
    slug_url_kwarg = 'slug'

    def get(self, request, *args, **kwargs):
        studio = get_object_or_404(Studio, slug=self.kwargs['slug'])
        context = {}
        obj, created = StudioStatistic.objects.get_or_create(
            defaults={
                "studio": studio,
                "date": timezone.now()
            },
            date=timezone.now(),
            studio=studio
        )

        obj.views += 1
        obj.save(update_fields=['views'])
        context['studio'] = studio
        context['config'] = config
        return render(
            request=request,
            template_name=self.template_name,
            context=context
        )


class StudioListView(ListView):
    model = Studio
    template_name = 'main/index.html'
    context_object_name = 'studios'

    def get_queryset(self):
        return Studio.objects.filter(
            when_it_ends__gt=timezone.now()
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        premium_studio_iist = self.get_queryset().filter(
            is_it_premium=True
        ).annotate(random_order=Random()).order_by('random_order')

        top_studios_list = self.get_queryset().filter(
            is_it_top=True,
            is_it_premium=False
        ).annotate(random_order=Random()).order_by('random_order')

        usuall_studios_list = self.get_queryset().filter(
            is_it_top=False,
            is_it_premium=False
        ).annotate(random_order=Random()).order_by('random_order')[:6]

        mini_ads = MiniAd.objects.filter(
            when_it_ends__gt=timezone.now()
        )

        for ad in mini_ads:
            obj, created = MiniAdStatistic.objects.get_or_create(
                defaults={
                    "mini_ad": ad,
                    "date": timezone.now()
                },
                date=timezone.now(), mini_ad=ad
            )

            obj.views += 1
            obj.save(update_fields=['views'])

        context['premium_studios_list'] = premium_studio_iist

        context['all_studios_list'] = list(chain(
            premium_studio_iist,
            top_studios_list,
            usuall_studios_list
        ))
        context['form'] = StudioSearchForm(self.request.GET)
        context['mini_ads'] = MiniAd.objects.filter(
            when_it_ends__gt=timezone.now()
        )
        context['config'] = config
        return context


class StudioSearchList(ListView):
    model = Studio
    template_name = 'main/search.html'
    context_object_name = 'studios'
    paginate_by = 12

    def get_queryset(self):
        queryset = Studio.objects.filter(
            when_it_ends__gt=timezone.now()
        )
        form = StudioSearchForm(self.request.GET)
        if form.is_valid():
            experiences = form.cleaned_data.get('experience')
            cities = form.cleaned_data.get('cities')
            format = form.cleaned_data.get('format')
            gender = form.cleaned_data.get('gender')
            if experiences:
                queryset = queryset.filter(experience__in=experiences)
            if cities:
                queryset = queryset.filter(cities__in=cities)
            if format:
                queryset = queryset.filter(format__in=format)
            if gender:
                queryset = queryset.filter(gender__in=gender)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        premium_studio_iist = self.get_queryset().filter(
            is_it_premium=True
        ).annotate(random_order=Random()).order_by('random_order')

        top_studios_list = self.get_queryset().filter(
            is_it_top=True,
            is_it_premium=False
        ).annotate(random_order=Random()).order_by('random_order')

        usuall_studios_list = self.get_queryset().filter(
            is_it_top=False,
            is_it_premium=False
        ).annotate(random_order=Random()).order_by('random_order')[:6]

        studios_list = list(chain(premium_studio_iist, top_studios_list, usuall_studios_list))

        context = super().get_context_data(**kwargs)
        context['form'] = StudioSearchForm(self.request.GET)
        context['config'] = config
        context['studios_list'] = studios_list
        return context
