from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Article, ArticleAdmin)
