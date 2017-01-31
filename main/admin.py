from django.contrib import admin
from main.models import Stock, Portfolio
# Register your models here.


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'last_price',)


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    pass
