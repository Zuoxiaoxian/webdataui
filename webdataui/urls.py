from django.conf.urls import include, url
from django.contrib import admin

from webdataui import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^aa/', views.home, name='home'),
]
