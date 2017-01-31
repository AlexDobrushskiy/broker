"""broker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from main import views as main_views
urlpatterns = [
    url(r'^admin/?', admin.site.urls),
    url(r'^stock_import', main_views.StockImportFormView.as_view(), name='stock-import'),
    url(r'^portfolio_import', main_views.PortfolioImportFormView.as_view(), name='portfolio-import'),
    url(r'^generate', main_views.GenerateResultView.as_view(), name='generate'),
    url(r'', main_views.root_view)
]
