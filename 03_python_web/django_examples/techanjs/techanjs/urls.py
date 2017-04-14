"""techanjs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.shortcuts import render

import pandas as pd
import pandas_datareader.data as web
from datetime import datetime

def index(request):
    df=web.DataReader("^DJI", 'yahoo', datetime(2016,1,1))
    df.sort_index(ascending=False)
    df[['Open','High','Low','Close','Volume']].to_csv("static/data.csv", date_format="%d-%b-%y")
    return render(request, 'index.html', {"symbol":"Dow Jones Index"})

def draw(request, symbol):
    df=web.DataReader(symbol, 'yahoo', datetime(2016,1,1))
    df.sort_index(ascending=False)
    df[['Open','High','Low','Close','Volume']].to_csv("static/data.csv", date_format="%d-%b-%y")
    return render(request, 'index.html', locals())

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^(?P<symbol>\w+)$', draw),
]
