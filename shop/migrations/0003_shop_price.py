# Generated by Django 4.2 on 2023-05-08 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_rename_date_shop_created_at_shop_likes_shop_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
