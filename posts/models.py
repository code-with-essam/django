from collections import _OrderedDictItemsView
from typing import OrderedDict
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Article(models.Model) :
    name = models.TextField(blank=True, null=True)
    image_post = models.ImageField(upload_to="posts", blank=True, null=True)
    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return f"this article created by {str(self.auther)} article name {self.name}"
    def detail_article(self) :
        return reverse("posts:detail", kwargs={"id":self.id})
    def update_article(self) :
        return reverse("posts:update", kwargs={"id":self.id})

    def delete_article(self) :
        return reverse("posts:delete", kwargs={"id":self.id})

