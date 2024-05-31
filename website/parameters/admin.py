from django.contrib import admin

from .models import (City, ExperienceChoices, FormatChoices, GenderChoices,
                     PayoutsChoices, ShiftsChoices)

admin.site.register(City)
admin.site.register(ExperienceChoices)
admin.site.register(FormatChoices)
admin.site.register(GenderChoices)
admin.site.register(PayoutsChoices)
admin.site.register(ShiftsChoices)
