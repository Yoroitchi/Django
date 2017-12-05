from django.http import HttpResponse,Http404
from django.utils import timezone
from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Article
from .forms import ContactForm, ArticleForm

def accueil(request):
    """ Afficher tous les articles de notre blog """
    articles = Article.objects.all() # Nous sélectionnons tous nos articles
    return render(request, 'accueil.html', {'derniers_articles': articles})

def sarrasin(request):
    " Afficher uniquement les crêpes classées dans la Categorie Sarrasin"
    articles = Article.objects.filter(categorie__nom__contains="Sarrasin")
    return render(request,'sarrasin.html',{'galettes_sarrasin': articles})

def sucree(request):
    " Afficher uniquement les crêpes classées dans la Categorie Sucrée"
    articles = Article.objects.filter(categorie__nom__contains="Sucrée")
    return render(request,'sucree.html',{'crepes_sucrees': articles})

def lire(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'lire.html', {'article':article})

def today_date(request):
    return render(request, 'date.html', {'date': datetime.now()})

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

    return render(request, 'contact.html', locals())

def add(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(accueil)
    return render(request, 'addarticle.html', locals())

def editArticle(request,id):
    article = get_object_or_404(Article, id=id)
    form = ArticleForm(request.POST or None, instance=article)
    if form.is_valid():
        form.save()
        return redirect(accueil)
    return render(request,'editArticle.html',locals())

def delete(request, id):
    Article.objects.filter(id=id).delete()
    return redirect(accueil)
