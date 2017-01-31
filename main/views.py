import io
import csv

from decimal import Decimal
from django.core.exceptions import ObjectDoesNotExist

from django.shortcuts import render
from django.views.generic.edit import FormView
from django import forms
from main.models import Stock, Portfolio, ResultView


def root_view(request):
    form = GenerateResultForm()
    return render(request, 'root.html', context={'form': form})


def get_client_code_choices():
    return [(y, y,) for y in {x[0] for x in Portfolio.objects.values_list('client_code')}]


class GenerateResultForm(forms.Form):
    client_code = forms.ChoiceField(choices=get_client_code_choices)

    def generate_view(self):
        client_code = self.cleaned_data['client_code']
        ResultView.objects.all().delete()
        stocks = Stock.objects.all()
        for stock in stocks:
            try:
                portfolio = Portfolio.objects.get(code=stock.code, client_code=client_code)
            except ObjectDoesNotExist:
                continue
            percent_diff = 100*(stock.last_price - portfolio.acquisition_price)/portfolio.acquisition_price
            ResultView.objects.create(name=stock.name, code=stock.code, buy_price=portfolio.acquisition_price,
                                      cur_price=stock.last_price, amount=portfolio.total, percent_diff=percent_diff)


class GenerateResultView(FormView):
    form_class = GenerateResultForm
    success_url = '/'

    def form_valid(self, form):
        form.generate_view()
        return super(GenerateResultView, self).form_valid(form)


class StockImportForm(forms.Form):
    import_data = forms.CharField(widget=forms.Textarea)

    def process_data(self):
        # Delete all from Stocks table
        Stock.objects.all().delete()
        # Parse data like csv
        data = self.cleaned_data.get('import_data')
        f = io.StringIO(data)
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            if len(row) < 4:  # header
                continue
            name, price, code = row[0], row[1], row[3]
            # create new Stocks model for each row
            Stock.objects.create(name=name, code=code, last_price=Decimal(price.replace(',', '.')))


class PortfolioImportForm(forms.Form):
    import_data = forms.CharField(widget=forms.Textarea)

    def process_data(self):
        # Delete all from Stocks table
        Portfolio.objects.all().delete()
        # Parse data like csv
        data = self.cleaned_data.get('import_data')
        f = io.StringIO(data)
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            if len(row) < 7:  # header
                continue

            # create new Portfolio model for each row
            name, code, client_code, total, acquisition_price = row[1], row[2], row[3], row[4], row[5]
            total = int(total.split(',')[0])
            acquisition_price = Decimal(acquisition_price.replace(',', '.'))
            Portfolio.objects.create(name=name, code=code, client_code=client_code, total=total,
                                     acquisition_price=acquisition_price)


class StockImportFormView(FormView):
    template_name = 'stock_import.html'
    form_class = StockImportForm
    success_url = '/'

    def form_valid(self, form):
        form.process_data()
        return super(StockImportFormView, self).form_valid(form)


class PortfolioImportFormView(FormView):
    template_name = 'portfolio_import.html'
    form_class = PortfolioImportForm
    success_url = '/'

    def form_valid(self, form):
        form.process_data()
        return super(PortfolioImportFormView, self).form_valid(form)
