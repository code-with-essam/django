from django.contrib import admin
from .models import Article
# Register your models here.

class ArticleAdmin(admin.ModelAdmin) :
    list_display = ["auther","name", "image_post", "timestamp", "updated"]
    search_fields = ["name"]

admin.site.register(Article, ArticleAdmin)