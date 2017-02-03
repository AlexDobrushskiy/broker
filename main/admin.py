from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from main.models import Stock, Portfolio, ResultView, Dividend


class ResultViewListFilter(SimpleListFilter):
    title = 'paper_type'
    parameter_name = 'paper_type'

    def lookups(self, request, model_admin):
            """
            Returns a list of tuples. The first element in each
            tuple is the coded value for the option that will
            appear in the URL query. The second element is the
            human-readable name for the option that will appear
            in the right sidebar.
            """
            return (
                ('stocks', 'stocks'),
                ('bonds', 'bonds'),
                ('stocks_in_portfolio', 'stocks_in_portfolio'),
            )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        if self.value() == 'stocks':
            return queryset.extra(where=["length(code) < 6"])
        if self.value() == 'bonds':
            return queryset.extra(where=["length(code) > 6"])
        if self.value() == 'stocks_in_portfolio':
            return queryset.extra(where=["length(code) < 6"]).exclude(amount__isnull=True)


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'last_price',)


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'client_code', 'total', 'acquisition_price',)


@admin.register(ResultView)
class ResultViewAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'buy_price', 'amount', 'cur_price', 'percent_diff', 'comment', 'has_dividends', 'divident_year_percent',)
    list_filter = (ResultViewListFilter,)


@admin.register(Dividend)
class DividendAdmin(admin.ModelAdmin):
    list_display = ('code', 'has_dividends', 'year_amount',)

