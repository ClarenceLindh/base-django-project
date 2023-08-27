from django.contrib import admin

from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'body', 'created_at', 'image', 'views', 'likes')
    list_filter = ('id', 'title', 'slug', 'body', 'created_at', 'image', 'views', 'likes')
    search_fields = ('id', 'title', 'slug', 'body', 'created_at', 'image', 'views', 'likes')
    ordering = ('id', 'title', 'slug', 'body', 'created_at', 'image', 'views', 'likes')

admin.site.register(Article, ArticleAdmin)
