from django.urls import path
from .views import ArticleListView, ArticleDetailView

urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('<slug:slug>/', ArticleDetailView.as_view(), name='get_article_by_slug')
]
