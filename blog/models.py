from django.db import models

# Create your models here.
from django.urls import reverse
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(verbose_name="Category", max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def get_absolute_url(self):
        return reverse("category_list", kwargs={"pk": self.pk})

class Article(models.Model):
    title = models.CharField(verbose_name="Title", max_length=255)
    description = models.TextField(verbose_name="Description")
    photo = models.ImageField(upload_to="photos/", blank=True, null=True)
    viewed = models.PositiveIntegerField(verbose_name="Views", default=0)
    published_date = models.DateTimeField(verbose_name="The date of publication", auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name="The date of update", auto_now_add=True)
    category = models.ForeignKey(Category, default=None, null=True, on_delete=models.CASCADE)
    author = models.ForeignKey(User, default=None, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def trim_description(self):
        return self.description if len(str(self.description)) < 100 else self.description[:100] + "..."

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk})


    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text