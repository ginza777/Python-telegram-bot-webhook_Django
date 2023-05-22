from django.contrib import admin

# Register your models here.
from .models import Region, Country
admin.site.register(Region)
admin.site.register(Country)