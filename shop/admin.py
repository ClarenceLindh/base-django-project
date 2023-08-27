from django.contrib import admin

from .models import Shop


class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_at', 'image', 'views', 'likes')
    list_filter = ('id', 'name', 'description', 'created_at', 'image', 'views', 'likes')
    search_fields = ('id', 'name', 'description', 'created_at', 'image', 'views', 'likes')
    ordering = ('id', 'name', 'description', 'created_at', 'image', 'views', 'likes')


admin.site.register(Shop, ShopAdmin)
