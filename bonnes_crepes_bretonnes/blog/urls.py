from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^accueil$', views.home),
    url(r'^article/(\d+)$',views.article),
    url(r'^date$', views.today_date),
]
