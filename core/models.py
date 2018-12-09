from django.db import models
from django.contrib.auth import get_user_model
from markdown import markdown
from django.utils.text import slugify
from django.db.models import Q
from django.utils import timezone
import uuid

usermodel = get_user_model()

class BaseThing(models.Model):
    tid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True

class Article(BaseThing):
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField(usermodel)
    published_after = models.DateTimeField(blank=True, null=True)
    published_until = models.DateTimeField(blank=True, null=True)
    content = models.TextField(blank=True, default='')
    rendered = models.TextField(blank=True, default='', editable=False)
    slug = models.SlugField(max_length=64, unique=True, default='')
    published = models.BooleanField(default=False)

    @property
    def author_names(self):
        return ', '.join([a.friendly_name for a in self.authors.all()])

    def __str__(self):
        return f"\"{self.title}\" ({self.author_names})"

    @classmethod
    def get_all_published(cls):
        now = timezone.now()
        return cls.objects.filter(
            Q(published=True),
            Q(published_after__isnull=True) | Q(published_after__lt=now),
            Q(published_until__isnull=True) | Q(published_until__gte=now)
        )

    def render(self):
        self.rendered = markdown(self.content, extensions=('core.mdext.fencer', 'codehilite', 'smarty'))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.render()
        super().save(*args, **kwargs)

