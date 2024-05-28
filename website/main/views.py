from itertools import chain

from constance import config
from django.db.models import BooleanField, Case, Value, When
from django.db.models.functions import Random
from django.utils import timezone
from django.views.generic import DetailView, ListView

from .forms import StudioSearchForm
from .models import MiniAd, Studio


class StudioDetailView(DetailView):
    model = Studio
    template_name = 'main/studio.html'
    context_object_name = 'studio'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['config'] = config
        return context


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

        top_studios_list = self.get_queryset().filter(
            is_it_top=True
        ).annotate(random_order=Random()).order_by('random_order')

        usuall_studios_list = self.get_queryset().filter(
            is_it_top=False, is_it_premium=False
        ).annotate(random_order=Random()).order_by('random_order')[:6]

        premium_studio_iist = self.get_queryset().filter(
            is_it_premium=True
        ).annotate(random_order=Random()).order_by('random_order')

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
        queryset = super().get_queryset()
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
        queryset = queryset.annotate(
            is_it_top_boolean=Case(
                When(is_it_top=True, then=Value(True)),
                default=Value(False),
                output_field=BooleanField(),
            )
        ).order_by('-is_it_top_boolean', '?')
        return queryset.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = StudioSearchForm(self.request.GET)
        context['config'] = config
        return context
