
from django import forms

from .models import City, ExperienceChoices, FormatChoices, GenderChoices


class StudioSearchForm(forms.Form):

    cities = forms.ModelMultipleChoiceField(
        queryset=City.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Города'
    )

    format = forms.ModelMultipleChoiceField(
        queryset=FormatChoices.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Формат работы'
    )

    experience = forms.ModelMultipleChoiceField(
        queryset=ExperienceChoices.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Опыт работы'
    )

    gender = forms.ModelMultipleChoiceField(
        queryset=GenderChoices.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Гендер',
    )
