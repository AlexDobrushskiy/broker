import io
import csv

from decimal import Decimal

from django.shortcuts import render
from django.views.generic.edit import FormView
from django import forms
from main.models import Stock


def root_view(request):
    return render(request, 'root.html')


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


class StockImportFormView(FormView):
    template_name = 'stock_import.html'
    form_class = StockImportForm
    success_url = '/'

    def form_valid(self, form):
        form.process_data()
        return super(StockImportFormView, self).form_valid(form)