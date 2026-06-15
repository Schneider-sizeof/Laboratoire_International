"""
Database models for Laboratoire International.
Blog system and contact form submissions.
"""
from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.conf import settings


class BlogCategory(models.Model):
    """Blog post categories."""
    slug = models.SlugField(max_length=100, unique=True)
    name_fr = models.CharField(max_length=200, verbose_name="Nom (FR)")
    name_en = models.CharField(max_length=200, blank=True, verbose_name="Name (EN)")
    name_ar = models.CharField(max_length=200, blank=True, verbose_name="الاسم (AR)")
    name_nl = models.CharField(max_length=200, blank=True, verbose_name="Naam (NL)")
    name_de = models.CharField(max_length=200, blank=True, verbose_name="Name (DE)")
    name_es = models.CharField(max_length=200, blank=True, verbose_name="Nombre (ES)")
    icon = models.CharField(max_length=50, default='fas fa-folder', help_text="FontAwesome icon class")
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Blog Category"
        verbose_name_plural = "Blog Categories"
        ordering = ['order', 'name_fr']

    def __str__(self):
        return self.name_fr

    def get_name(self, lang='fr'):
        """Get the localized category name."""
        name = getattr(self, f'name_{lang}', '') or self.name_fr
        return name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name_fr)
        super().save(*args, **kwargs)


class BlogPost(models.Model):
    """Blog posts with multi-language support."""
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]

    slug = models.SlugField(max_length=200, unique=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    category = models.ForeignKey(
        BlogCategory, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='posts'
    )
    featured_image = models.ImageField(upload_to='blog/', blank=True, null=True)
    author = models.CharField(max_length=200, default='Laboratoire International')
    tags = models.CharField(max_length=500, blank=True, help_text="Comma-separated tags")
    views_count = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)

    # French content (default/required)
    title_fr = models.CharField(max_length=300, verbose_name="Titre (FR)")
    excerpt_fr = models.TextField(max_length=500, blank=True, verbose_name="Extrait (FR)")
    content_fr = models.TextField(verbose_name="Contenu (FR)")
    meta_title_fr = models.CharField(max_length=70, blank=True, verbose_name="Meta Title (FR)")
    meta_description_fr = models.CharField(max_length=160, blank=True, verbose_name="Meta Description (FR)")

    # English content
    title_en = models.CharField(max_length=300, blank=True, verbose_name="Title (EN)")
    excerpt_en = models.TextField(max_length=500, blank=True, verbose_name="Excerpt (EN)")
    content_en = models.TextField(blank=True, verbose_name="Content (EN)")
    meta_title_en = models.CharField(max_length=70, blank=True, verbose_name="Meta Title (EN)")
    meta_description_en = models.CharField(max_length=160, blank=True, verbose_name="Meta Description (EN)")

    # Arabic content
    title_ar = models.CharField(max_length=300, blank=True, verbose_name="العنوان (AR)")
    excerpt_ar = models.TextField(max_length=500, blank=True, verbose_name="مقتطف (AR)")
    content_ar = models.TextField(blank=True, verbose_name="المحتوى (AR)")
    meta_title_ar = models.CharField(max_length=70, blank=True, verbose_name="Meta Title (AR)")
    meta_description_ar = models.CharField(max_length=160, blank=True, verbose_name="Meta Description (AR)")

    # Dutch content
    title_nl = models.CharField(max_length=300, blank=True, verbose_name="Titel (NL)")
    excerpt_nl = models.TextField(max_length=500, blank=True, verbose_name="Excerpt (NL)")
    content_nl = models.TextField(blank=True, verbose_name="Inhoud (NL)")
    meta_title_nl = models.CharField(max_length=70, blank=True, verbose_name="Meta Title (NL)")
    meta_description_nl = models.CharField(max_length=160, blank=True, verbose_name="Meta Description (NL)")

    # German content
    title_de = models.CharField(max_length=300, blank=True, verbose_name="Titel (DE)")
    excerpt_de = models.TextField(max_length=500, blank=True, verbose_name="Auszug (DE)")
    content_de = models.TextField(blank=True, verbose_name="Inhalt (DE)")
    meta_title_de = models.CharField(max_length=70, blank=True, verbose_name="Meta Title (DE)")
    meta_description_de = models.CharField(max_length=160, blank=True, verbose_name="Meta Description (DE)")

    # Spanish content
    title_es = models.CharField(max_length=300, blank=True, verbose_name="Título (ES)")
    excerpt_es = models.TextField(max_length=500, blank=True, verbose_name="Extracto (ES)")
    content_es = models.TextField(blank=True, verbose_name="Contenido (ES)")
    meta_title_es = models.CharField(max_length=70, blank=True, verbose_name="Meta Title (ES)")
    meta_description_es = models.CharField(max_length=160, blank=True, verbose_name="Meta Description (ES)")

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
        ordering = ['-published_at', '-created_at']

    def __str__(self):
        return self.title_fr

    def get_title(self, lang='fr'):
        return getattr(self, f'title_{lang}', '') or self.title_fr

    def get_excerpt(self, lang='fr'):
        return getattr(self, f'excerpt_{lang}', '') or self.excerpt_fr

    def get_content(self, lang='fr'):
        return getattr(self, f'content_{lang}', '') or self.content_fr

    def get_meta_title(self, lang='fr'):
        return getattr(self, f'meta_title_{lang}', '') or self.get_title(lang)

    def get_meta_description(self, lang='fr'):
        return getattr(self, f'meta_description_{lang}', '') or self.get_excerpt(lang)[:160]

    def get_tags_list(self):
        if self.tags:
            return [tag.strip() for tag in self.tags.split(',') if tag.strip()]
        return []

    def publish(self):
        self.status = 'published'
        self.published_at = timezone.now()
        self.save()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title_fr)
        super().save(*args, **kwargs)


class ContactSubmission(models.Model):
    """Contact form submissions stored in database."""
    SERVICE_CHOICES = [
        ('general', 'Renseignements généraux'),
        ('results', 'Résultats d\'analyses'),
        ('appointment', 'Prise de rendez-vous'),
        ('partnership', 'Partenariat'),
        ('complaint', 'Réclamation'),
        ('other', 'Autre'),
    ]

    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES, default='general')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    admin_notes = models.TextField(blank=True)

    class Meta:
        verbose_name = "Contact Submission"
        verbose_name_plural = "Contact Submissions"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} — {self.get_service_type_display()} ({self.created_at.strftime('%d/%m/%Y')})"
