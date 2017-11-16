from django.contrib import admin
from .models import Categorie,Article
from django.utils.text import Truncator

class ArticleAdmin(admin.ModelAdmin):
    fields = ('titre', 'auteur', 'categorie', 'ingredients','preparation')
    list_display   = ('titre','categorie', 'auteur', 'date', 'apercu_ingredient', 'apercu_preparation')
    list_filter    = ('auteur','categorie',)
    date_hierarchy = 'date'
    ordering       = ('date', )
    search_fields  = ('titre', 'auteur')

    def apercu_ingredient(self, article):
        return Truncator(article.ingredients).chars(40, truncate='...')

    def apercu_preparation(self, article):
        return Truncator(article.preparation).chars(40, truncate='...')

admin.site.register(Categorie)
admin.site.register(Article,ArticleAdmin)
