from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Cards, CardsZhcn

admin.site.register(Cards)
admin.site.register(CardsZhcn)
