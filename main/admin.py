from django.contrib import admin
from main.models import Stock, Portfolio, ResultView, Dividend


# Register your models here.


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'last_price',)


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'client_code', 'total', 'acquisition_price',)


@admin.register(ResultView)
class ResultViewAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'buy_price', 'amount', 'cur_price', 'percent_diff', 'comment', 'has_dividends', 'divident_year_percent',)


@admin.register(Dividend)
class DividendAdmin(admin.ModelAdmin):
    list_display = ('code', 'has_dividends', 'year_amount',)

