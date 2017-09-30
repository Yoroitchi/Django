from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

def home(request):
    text = "Hola ketal !"
    return HttpResponse(text)

def article(request, ID_article):
    #Put here the views related to an article
    return HttpResponse("You asked for the #{0} article.".format(ID_article))

def today_date(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})
