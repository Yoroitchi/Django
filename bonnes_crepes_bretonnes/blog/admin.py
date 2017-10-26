from django.contrib import admin
from .models import Categorie, Article
from django.utils.text import Truncator

class ArticleAdmin(admin.ModelAdmin):
    fields = ('titre', 'slug', 'auteur', 'categorie', 'contenu')
    list_display   = ('titre','categorie', 'auteur', 'date', 'apercu_contenu')
    list_filter    = ('auteur','categorie',)
    date_hierarchy = 'date'
    ordering       = ('date', )
    search_fields  = ('titre', 'contenu')
    prepopulated_fields = {'slug': ('titre', ), }

    def apercu_contenu(self, article):
        return Truncator(article.contenu).chars(40, truncate='...')

admin.site.register(Categorie)
admin.site.register(Article,ArticleAdmin)
