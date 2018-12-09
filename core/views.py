from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Q
from django.utils import timezone

from .models import Article

class ArticleListView(ListView):

    template_name = 'article_list.html'
    paginate_by = 100  # if pagination is desired

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['now'] = timezone.now()
    #     return context

    def get_queryset(self):
        return Article.get_all_published().order_by('-created_at')

class ArticleDetailView(DetailView):
    template_name = 'article_detail.html'
    model = Article

    def get_queryset(self):
        now = timezone.now()
        qs = super().get_queryset()
        return qs.filter(
            Q(published=True),
            Q(published_after__isnull=True) | Q(published_after__lt=now),
            Q(published_until__isnull=True) | Q(published_until__gte=now)
        )


