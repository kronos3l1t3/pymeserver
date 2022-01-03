from django.contrib import admin
from .models import Country, Location, Coin, Gateway


# Register your models here.
admin.site.register(Country)
admin.site.register(Location)
admin.site.register(Coin)
admin.site.register(Gateway)
