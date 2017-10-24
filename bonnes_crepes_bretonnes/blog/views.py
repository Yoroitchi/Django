from django.http import HttpResponse,Http404
from django.utils import timezone
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from blog.models import Article

def home(request):
    return render(request, 'blog/home.html', {'date': datetime.now()})

def accueil(request):
    """ Afficher tous les articles de notre blog """
    articles = Article.objects.all() # Nous sélectionnons tous nos articles
    return render(request, 'blog/accueil.html', {'derniers_articles': articles})

def lire(request, id, slug):
    article = get_object_or_404(Article, id=id, slug=slug)
    return render(request, 'blog/lire.html', {'article':article})

def today_date(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})
