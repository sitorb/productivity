from django.contrib import admin

from .models import Article, Category


# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "trim_description", "viewed", "published_date", "updated_date", "category", "author")
    list_display_links = ("id", "title")
    list_editable = ("category", "author")
    list_filter = ("published_date", "category", "author")

    def trim_description(self, obj):
        return obj.description if len(str(obj.description)) < 100 else obj.description[:100] + "..."

    trim_description.short_description = "Description"


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
