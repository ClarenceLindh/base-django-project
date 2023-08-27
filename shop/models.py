from django.db import models

# Create your models here.

class Shop(models.Model):
    class Meta:
        verbose_name = 'Shop'
        db_table = 'shop'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.png', blank=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
