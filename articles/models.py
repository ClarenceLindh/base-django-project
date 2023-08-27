from django.db import models


class Article(models.Model):
    class Meta:
        verbose_name = "Article"
        db_table = "article"

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(default="default", unique=True)
    summary = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.CharField(blank=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
