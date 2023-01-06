from django.contrib import admin
from .models import RadioModel


@admin.register(RadioModel)
class RadioModelAdmin(admin.ModelAdmin):
    list_display = ['spam']

