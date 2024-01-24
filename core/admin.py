from django.contrib import admin

from .models import About, Card, PersonalData

# Register your models here.
admin.site.register(PersonalData)
admin.site.register(About)
admin.site.register(Card)
