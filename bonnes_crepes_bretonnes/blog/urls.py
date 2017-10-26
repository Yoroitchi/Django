from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^home$', views.home, name='home'),
    url(r'^accueil$', views.accueil, name='accueil'),
    url(r'^article/(?P<id>\d+)-(?P<slug>.+)$',views.lire, name='lire'),
    url(r'^date$', views.today_date),
    url(r'^contact/$', views.contact, name='contact'),
]
