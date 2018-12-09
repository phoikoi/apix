from django.contrib import admin
from .models import Article
from pagedown.widgets import AdminPagedownWidget
from django.db import models

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    readonly_fields = ('slug',)
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }
