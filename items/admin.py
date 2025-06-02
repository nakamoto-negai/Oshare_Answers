from django.contrib import admin
from django.contrib import admin
from .models import Category, Item, StockHistory, Recommendation

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(StockHistory)
admin.site.register(Recommendation)
# Register your models here.
