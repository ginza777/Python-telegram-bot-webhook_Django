from django.contrib import admin
from .models import TelegramProfile,Country,Region


# Register your models here.
@admin.register(TelegramProfile)
class TelegramProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','username','telegram_id']

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['name','country']