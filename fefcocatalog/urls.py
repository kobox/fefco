__author__ = 'ko'
from django.conf.urls import url
from . import views
from .models import FefcoCategory

urlpatterns = [
    #url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/$', views.DetailView.as_view(model=FefcoCategory), name='detail'),
    ]