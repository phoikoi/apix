from django import template
register = template.Library()
from core.models import Article
from django.utils import timezone
from django.db.models import Q

@register.inclusion_tag('leftbar_article_list.html')
def show_article_list():
    articles = Article.get_all_published().order_by('-created_at')
    return dict(articles=articles[:10])
