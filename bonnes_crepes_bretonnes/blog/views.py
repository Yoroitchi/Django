from django.http import HttpResponse,Http404
from django.utils import timezone
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from blog.models import Article
from .forms import ContactForm

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

def contact(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.

    form = ContactForm(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données
    # dans le formulaire ou qu'il contient des erreurs.

    if form.is_valid():
        sujet = form.cleaned_data['sujet']
        message = form.cleaned_data['message']
        envoyeur = form.cleaned_data['envoyeur']
        renvoi = form.cleaned_data['renvoi']
        envoi = True

    return render(request, 'blog/contact.html', locals())
