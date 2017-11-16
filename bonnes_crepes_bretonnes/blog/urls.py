from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^home$', views.home, name='home'),
    url(r'^accueil$', views.accueil, name='accueil'),
    url(r'^article/(?P<id>\d+)$', views.lire, name='lire'),
    url(r'^galettes-de-sarrasin$', views.sarrasin, name='sarrasin'),
    url(r'^crepes-sucrees$', views.sucree, name='sucree'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^add/$',views.add,name='addarticle'),
    url(r'^editArticle/(?P<id>\d+)$', views.editArticle, name='edit'),
    url(r'^deleteArticle/(?P<id>\d+)$', views.delete, name='delete'),
]
