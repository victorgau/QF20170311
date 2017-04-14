from django.conf.urls import url
from .views import hello

urlpatterns = [
    url(r'^$', hello),
]
