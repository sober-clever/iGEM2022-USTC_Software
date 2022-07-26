from django.contrib import admin
from testapp.models import Article


# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
