"""
Database models for Laboratoire International.
SiteSettings, Team, Partners, Blog, and Contact submissions.
"""
from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.conf import settings
from django.core.cache import cache


# ============================================================
# Site Settings (Singleton)
# ============================================================
class SiteSettings(models.Model):
    """
    Singleton model for site-wide configuration.
    Editable from Django admin — replaces hardcoded settings.
    """
    # General
    site_name = models.CharField(
        max_length=200, default='Laboratoire International Tanger',
        verbose_name="Nom du site"
    )
    site_slogan_fr = models.CharField(
        max_length=300, default='Votre santé est Notre priorité',
        verbose_name="Slogan (FR)"
    )
    site_slogan_en = models.CharField(
        max_length=300, blank=True, default='Your health is Our priority',
        verbose_name="Slogan (EN)"
    )
    site_slogan_ar = models.CharField(
        max_length=300, blank=True, default='صحتكم أولويتنا',
        verbose_name="Slogan (AR)"
    )
    site_slogan_es = models.CharField(
        max_length=300, blank=True, default='Su salud es Nuestra prioridad',
        verbose_name="Slogan (ES)"
    )
    site_slogan_de = models.CharField(
        max_length=300, blank=True, default='Ihre Gesundheit ist Unsere Priorität',
        verbose_name="Slogan (DE)"
    )
    site_slogan_nl = models.CharField(
        max_length=300, blank=True, default='Uw gezondheid is Onze prioriteit',
        verbose_name="Slogan (NL)"
    )
    site_slogan_it = models.CharField(
        max_length=300, blank=True, default='La vostra salute è la Nostra priorità',
        verbose_name="Slogan (IT)"
    )
    site_domain = models.CharField(
        max_length=200, default='laboratoiretanger.com',
        verbose_name="Domaine"
    )

    # Contact
    phone = models.CharField(
        max_length=30, default='+212 5 39 31 39 47',
        verbose_name="Téléphone"
    )
    email = models.EmailField(
        default='contact@laboratoiretanger.com',
        verbose_name="Email"
    )
    whatsapp = models.CharField(
        max_length=30, default='212539313947',
        verbose_name="WhatsApp (numéro sans +)",
        help_text="Format: 212XXXXXXXXX (sans le +)"
    )
    address = models.CharField(
        max_length=300, default='Avenue Moulay Rachid, Tanger 90000, Morocco',
        verbose_name="Adresse"
    )
    maps_url = models.URLField(
        blank=True, default='https://maps.app.goo.gl/HSkgrJB5ffH6xe727',
        verbose_name="Google Maps URL"
    )
    maps_embed = models.TextField(
        blank=True,
        default='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3237.922853199904!2d-5.853466!3d35.7527009!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xd0b87bb4130edf5%3A0xb2bc80cfeb3a4755!2sLaboratoire%20International!5e0!3m2!1sen!2sma!4v1',
        verbose_name="Google Maps Embed URL"
    )

    # Opening Hours
    opening_hours = models.CharField(
        max_length=50, default='', blank=True,
        verbose_name="Horaires d'ouverture"
    )
    opening_days_fr = models.CharField(max_length=150, default='Lundi - Vendredi : 07:00 - 19:00 | Samedi : 07:00 - 15:00', verbose_name="Jours (FR)")
    opening_days_en = models.CharField(max_length=150, blank=True, default='Monday - Friday: 7:00 AM - 7:00 PM | Saturday: 7:00 AM - 3:00 PM', verbose_name="Days (EN)")
    opening_days_ar = models.CharField(max_length=150, blank=True, default='الإثنين - الجمعة: 07:00 - 19:00 | السبت: 07:00 - 15:00', verbose_name="Days (AR)")
    closed_day_fr = models.CharField(max_length=100, default='Dimanche: Fermé', verbose_name="Jour fermé (FR)")
    closed_day_en = models.CharField(max_length=100, blank=True, default='Sunday: Closed', verbose_name="Closed day (EN)")
    closed_day_ar = models.CharField(max_length=100, blank=True, default='الأحد: مغلق', verbose_name="Closed day (AR)")

    # Social Media
    facebook_url = models.URLField(blank=True, verbose_name="Facebook URL")
    instagram_url = models.URLField(blank=True, verbose_name="Instagram URL")
    linkedin_url = models.URLField(blank=True, verbose_name="LinkedIn URL")
    youtube_url = models.URLField(blank=True, verbose_name="YouTube URL")
    tiktok_url = models.URLField(blank=True, verbose_name="TikTok URL")

    # Analytics
    ga4_measurement_id = models.CharField(
        max_length=50, blank=True,
        verbose_name="Google Analytics 4 Measurement ID",
        help_text="Format: G-XXXXXXXXXX"
    )

    # VisionLIS
    visionlis_url = models.URLField(
        blank=True, default='http://liamt.ddns.net:12543/visionlis/#/loginpatient',
        verbose_name="VisionLIS Portal URL"
    )

    # Email Notifications
    notification_email = models.EmailField(
        blank=True,
        verbose_name="Email de notification",
        help_text="Adresse où les soumissions du formulaire de contact seront envoyées. Laisser vide pour désactiver."
    )
    smtp_host = models.CharField(max_length=200, blank=True, default='smtp.gmail.com', verbose_name="SMTP Host")
    smtp_port = models.IntegerField(default=587, verbose_name="SMTP Port")
    smtp_user = models.CharField(max_length=200, blank=True, verbose_name="SMTP User")
    smtp_password = models.CharField(max_length=200, blank=True, verbose_name="SMTP Password")
    smtp_use_tls = models.BooleanField(default=True, verbose_name="Use TLS")

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return self.site_name

    def get_slogan(self, lang=None):
        """Get the localized slogan."""
        from django.utils import translation
        if not lang:
            lang = translation.get_language() or 'fr'
        return getattr(self, f'site_slogan_{lang}', '') or self.site_slogan_fr

    def get_opening_days(self, lang=None):
        """Get localized opening days."""
        from django.utils import translation
        if not lang:
            lang = translation.get_language() or 'fr'
        return getattr(self, f'opening_days_{lang}', '') or self.opening_days_fr

    def get_closed_day(self, lang=None):
        """Get localized closed day."""
        from django.utils import translation
        if not lang:
            lang = translation.get_language() or 'fr'
        return getattr(self, f'closed_day_{lang}', '') or self.closed_day_fr

    def get_social_links(self):
        """Return a list of social links that are configured."""
        links = []
        if self.facebook_url:
            links.append({'name': 'Facebook', 'url': self.facebook_url, 'icon': 'fab fa-facebook-f', 'color': 'hover:bg-blue-600'})
        if self.instagram_url:
            links.append({'name': 'Instagram', 'url': self.instagram_url, 'icon': 'fab fa-instagram', 'color': 'hover:bg-pink-500'})
        if self.linkedin_url:
            links.append({'name': 'LinkedIn', 'url': self.linkedin_url, 'icon': 'fab fa-linkedin-in', 'color': 'hover:bg-blue-700'})
        if self.youtube_url:
            links.append({'name': 'YouTube', 'url': self.youtube_url, 'icon': 'fab fa-youtube', 'color': 'hover:bg-red-600'})
        if self.tiktok_url:
            links.append({'name': 'TikTok', 'url': self.tiktok_url, 'icon': 'fab fa-tiktok', 'color': 'hover:bg-dark-700'})
        if self.whatsapp:
            links.append({'name': 'WhatsApp', 'url': f'https://wa.me/{self.whatsapp}', 'icon': 'fab fa-whatsapp', 'color': 'hover:bg-green-500'})
        return links

    def save(self, *args, **kwargs):
        # Singleton: ensure only one instance exists
        self.pk = 1
        super().save(*args, **kwargs)
        # Clear cache when settings change
        cache.delete('site_settings')

    @classmethod
    def load(cls):
        """Load the singleton instance (cached)."""
        obj = cache.get('site_settings')
        if obj is None:
            obj, created = cls.objects.get_or_create(pk=1)
            cache.set('site_settings', obj, 300)  # Cache for 5 minutes
        return obj


# ============================================================
# Team Members
# ============================================================
class TeamMember(models.Model):
    """Team members displayed on about page — admin-editable."""
    name = models.CharField(max_length=200, verbose_name="Nom complet")
    initials = models.CharField(max_length=5, verbose_name="Initiales", help_text="Ex: YM, FB")
    photo = models.ImageField(upload_to='team/', blank=True, null=True, verbose_name="Photo")

    # Multilingual role
    role_fr = models.CharField(max_length=200, verbose_name="Rôle (FR)")
    role_en = models.CharField(max_length=200, blank=True, verbose_name="Role (EN)")
    role_ar = models.CharField(max_length=200, blank=True, verbose_name="الدور (AR)")
    role_es = models.CharField(max_length=200, blank=True, verbose_name="Rol (ES)")
    role_de = models.CharField(max_length=200, blank=True, verbose_name="Rolle (DE)")
    role_nl = models.CharField(max_length=200, blank=True, verbose_name="Rol (NL)")
    role_it = models.CharField(max_length=200, blank=True, verbose_name="Ruolo (IT)")

    # Multilingual bio
    bio_fr = models.TextField(verbose_name="Bio (FR)")
    bio_en = models.TextField(blank=True, verbose_name="Bio (EN)")
    bio_ar = models.TextField(blank=True, verbose_name="السيرة (AR)")
    bio_es = models.TextField(blank=True, verbose_name="Bio (ES)")
    bio_de = models.TextField(blank=True, verbose_name="Bio (DE)")
    bio_nl = models.TextField(blank=True, verbose_name="Bio (NL)")
    bio_it = models.TextField(blank=True, verbose_name="Bio (IT)")

    order = models.IntegerField(default=0, verbose_name="Ordre d'affichage")
    is_active = models.BooleanField(default=True, verbose_name="Actif")

    class Meta:
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} — {self.role_fr}"

    def get_role(self, lang=None):
        from django.utils import translation
        if not lang:
            lang = translation.get_language() or 'fr'
        return getattr(self, f'role_{lang}', '') or self.role_fr

    def get_bio(self, lang=None):
        from django.utils import translation
        if not lang:
            lang = translation.get_language() or 'fr'
        return getattr(self, f'bio_{lang}', '') or self.bio_fr


# ============================================================
# Partners / Collaborators
# ============================================================
class Partner(models.Model):
    """Partners and collaborators — admin-editable with logo upload."""
    name = models.CharField(max_length=200, verbose_name="Nom")
    logo = models.ImageField(upload_to='partners/', blank=True, null=True, verbose_name="Logo")
    icon = models.CharField(
        max_length=50, blank=True, default='fas fa-handshake',
        verbose_name="Icône FontAwesome",
        help_text="Utilisé si aucun logo n'est téléchargé. Ex: fas fa-globe-europe"
    )

    # Multilingual description
    description_fr = models.TextField(verbose_name="Description (FR)")
    description_en = models.TextField(blank=True, verbose_name="Description (EN)")
    description_ar = models.TextField(blank=True, verbose_name="الوصف (AR)")
    description_es = models.TextField(blank=True, verbose_name="Descripción (ES)")
    description_de = models.TextField(blank=True, verbose_name="Beschreibung (DE)")
    description_nl = models.TextField(blank=True, verbose_name="Beschrijving (NL)")
    description_it = models.TextField(blank=True, verbose_name="Descrizione (IT)")

    url = models.URLField(blank=True, verbose_name="Site web")
    order = models.IntegerField(default=0, verbose_name="Ordre d'affichage")
    is_active = models.BooleanField(default=True, verbose_name="Actif")

    class Meta:
        verbose_name = "Partner"
        verbose_name_plural = "Partners"
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

    def get_description(self, lang=None):
        from django.utils import translation
        if not lang:
            lang = translation.get_language() or 'fr'
        return getattr(self, f'description_{lang}', '') or self.description_fr


# ============================================================
# Blog Category
# ============================================================
class BlogCategory(models.Model):
    """Blog post categories."""
    slug = models.SlugField(max_length=100, unique=True)
    name_fr = models.CharField(max_length=200, verbose_name="Nom (FR)")
    name_en = models.CharField(max_length=200, blank=True, verbose_name="Name (EN)")
    name_ar = models.CharField(max_length=200, blank=True, verbose_name="الاسم (AR)")
    name_nl = models.CharField(max_length=200, blank=True, verbose_name="Naam (NL)")
    name_de = models.CharField(max_length=200, blank=True, verbose_name="Name (DE)")
    name_es = models.CharField(max_length=200, blank=True, verbose_name="Nombre (ES)")
    name_it = models.CharField(max_length=200, blank=True, verbose_name="Nome (IT)")
    icon = models.CharField(max_length=50, default='fas fa-folder', help_text="FontAwesome icon class")
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Blog Category"
        verbose_name_plural = "Blog Categories"
        ordering = ['order', 'name_fr']

    def __str__(self):
        return self.name_fr

    def get_name(self, lang=None):
        """Get the localized category name."""
        from django.utils import translation
        if not lang:
            lang = translation.get_language() or 'fr'
        name = getattr(self, f'name_{lang}', '') or self.name_fr
        return name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name_fr)
        super().save(*args, **kwargs)


# ============================================================
# Blog Post
# ============================================================
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
    author = models.CharField(max_length=200, default='Laboratoire International Tanger')
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

    # Italian content
    title_it = models.CharField(max_length=300, blank=True, verbose_name="Titolo (IT)")
    excerpt_it = models.TextField(max_length=500, blank=True, verbose_name="Estratto (IT)")
    content_it = models.TextField(blank=True, verbose_name="Contenuto (IT)")
    meta_title_it = models.CharField(max_length=70, blank=True, verbose_name="Meta Title (IT)")
    meta_description_it = models.CharField(max_length=160, blank=True, verbose_name="Meta Description (IT)")

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
        ordering = ['-published_at', '-created_at']

    def __str__(self):
        return self.title_fr

    def get_title(self, lang=None):
        from django.utils import translation
        if not lang:
            lang = translation.get_language() or 'fr'
        return getattr(self, f'title_{lang}', '') or self.title_fr

    def get_excerpt(self, lang=None):
        from django.utils import translation
        if not lang:
            lang = translation.get_language() or 'fr'
        return getattr(self, f'excerpt_{lang}', '') or self.excerpt_fr

    def get_content(self, lang=None):
        from django.utils import translation
        if not lang:
            lang = translation.get_language() or 'fr'
        return getattr(self, f'content_{lang}', '') or self.content_fr

    def get_meta_title(self, lang=None):
        from django.utils import translation
        if not lang:
            lang = translation.get_language() or 'fr'
        return getattr(self, f'meta_title_{lang}', '') or self.get_title(lang)

    def get_meta_description(self, lang=None):
        from django.utils import translation
        if not lang:
            lang = translation.get_language() or 'fr'
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


# ============================================================
# Contact Submission
# ============================================================
class ContactSubmission(models.Model):
    """Contact form submissions stored in database."""
    SERVICE_CHOICES = [
        ('general', 'Renseignements généraux'),
        ('results', "Résultats d'analyses"),
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


# ============================================================
# Analysis Category
# ============================================================
class AnalysisCategory(models.Model):
    """Categories for medical analyses (e.g., Biochimie, Hématologie)."""
    slug = models.SlugField(max_length=100, unique=True)
    name_fr = models.CharField(max_length=200, verbose_name="Nom (FR)")
    name_en = models.CharField(max_length=200, blank=True, verbose_name="Name (EN)")
    name_ar = models.CharField(max_length=200, blank=True, verbose_name="الاسم (AR)")
    name_nl = models.CharField(max_length=200, blank=True, verbose_name="Naam (NL)")
    name_de = models.CharField(max_length=200, blank=True, verbose_name="Name (DE)")
    name_es = models.CharField(max_length=200, blank=True, verbose_name="Nombre (ES)")
    name_it = models.CharField(max_length=200, blank=True, verbose_name="Nome (IT)")
    icon = models.CharField(max_length=50, default='fas fa-flask', help_text="FontAwesome icon class")
    color = models.CharField(max_length=20, default='primary')
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Analysis Category"
        verbose_name_plural = "Analysis Categories"
        ordering = ['order', 'name_fr']

    def __str__(self):
        return self.name_fr

    def get_name(self, lang=None):
        from django.utils import translation
        if not lang:
            lang = translation.get_language() or 'fr'
        return getattr(self, f'name_{lang}', '') or self.name_fr

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name_fr)
        super().save(*args, **kwargs)


# ============================================================
# Analysis (Individual test/profile page)
# ============================================================
class Analysis(models.Model):
    """Individual medical analysis with dedicated SEO page."""
    slug = models.SlugField(max_length=200, unique=True)
    category = models.ForeignKey(
        AnalysisCategory, on_delete=models.CASCADE,
        related_name='analyses'
    )
    icon = models.CharField(max_length=50, default='fas fa-vial', help_text="FontAwesome icon class")
    order = models.IntegerField(default=0)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # French (required)
    name_fr = models.CharField(max_length=300, verbose_name="Nom (FR)")
    description_fr = models.TextField(verbose_name="Description (FR)")
    why_fr = models.TextField(blank=True, verbose_name="Pourquoi faire cette analyse (FR)")
    delay_fr = models.CharField(max_length=200, blank=True, verbose_name="Délai résultat (FR)")
    meta_title_fr = models.CharField(max_length=70, blank=True, verbose_name="Meta Title (FR)")
    meta_description_fr = models.CharField(max_length=160, blank=True, verbose_name="Meta Description (FR)")

    # English
    name_en = models.CharField(max_length=300, blank=True, verbose_name="Name (EN)")
    description_en = models.TextField(blank=True, verbose_name="Description (EN)")
    why_en = models.TextField(blank=True, verbose_name="Why get this test (EN)")
    delay_en = models.CharField(max_length=200, blank=True, verbose_name="Result delay (EN)")
    meta_title_en = models.CharField(max_length=70, blank=True, verbose_name="Meta Title (EN)")
    meta_description_en = models.CharField(max_length=160, blank=True, verbose_name="Meta Description (EN)")

    # Arabic
    name_ar = models.CharField(max_length=300, blank=True, verbose_name="الاسم (AR)")
    description_ar = models.TextField(blank=True, verbose_name="الوصف (AR)")
    why_ar = models.TextField(blank=True, verbose_name="لماذا (AR)")
    delay_ar = models.CharField(max_length=200, blank=True, verbose_name="مدة النتيجة (AR)")
    meta_title_ar = models.CharField(max_length=70, blank=True, verbose_name="Meta Title (AR)")
    meta_description_ar = models.CharField(max_length=160, blank=True, verbose_name="Meta Description (AR)")

    # Dutch
    name_nl = models.CharField(max_length=300, blank=True)
    description_nl = models.TextField(blank=True)
    why_nl = models.TextField(blank=True)
    delay_nl = models.CharField(max_length=200, blank=True)

    # German
    name_de = models.CharField(max_length=300, blank=True)
    description_de = models.TextField(blank=True)
    why_de = models.TextField(blank=True)
    delay_de = models.CharField(max_length=200, blank=True)

    # Spanish
    name_es = models.CharField(max_length=300, blank=True)
    description_es = models.TextField(blank=True)
    why_es = models.TextField(blank=True)
    delay_es = models.CharField(max_length=200, blank=True)

    # Italian
    name_it = models.CharField(max_length=300, blank=True)
    description_it = models.TextField(blank=True)
    why_it = models.TextField(blank=True)
    delay_it = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = "Analysis"
        verbose_name_plural = "Analyses"
        ordering = ['category__order', 'order', 'name_fr']

    def __str__(self):
        return self.name_fr

    def get_name(self, lang=None):
        from django.utils import translation
        if not lang:
            lang = translation.get_language() or 'fr'
        return getattr(self, f'name_{lang}', '') or self.name_fr

    def get_description(self, lang=None):
        from django.utils import translation
        if not lang:
            lang = translation.get_language() or 'fr'
        return getattr(self, f'description_{lang}', '') or self.description_fr

    def get_why(self, lang=None):
        from django.utils import translation
        if not lang:
            lang = translation.get_language() or 'fr'
        return getattr(self, f'why_{lang}', '') or self.why_fr

    def get_delay(self, lang=None):
        from django.utils import translation
        if not lang:
            lang = translation.get_language() or 'fr'
        return getattr(self, f'delay_{lang}', '') or self.delay_fr

    def get_meta_title(self, lang=None):
        from django.utils import translation
        if not lang:
            lang = translation.get_language() or 'fr'
        meta = getattr(self, f'meta_title_{lang}', '')
        return meta or f"{self.get_name(lang)} — Tanger"

    def get_meta_description(self, lang=None):
        from django.utils import translation
        if not lang:
            lang = translation.get_language() or 'fr'
        meta = getattr(self, f'meta_description_{lang}', '')
        return meta or self.get_description(lang)[:160]

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('core:analysis_detail', kwargs={'slug': self.slug})


# ============================================================
# Neighborhood Page (local SEO)
# ============================================================
class NeighborhoodPage(models.Model):
    """Local/neighborhood pages for geographic SEO targeting."""
    slug = models.SlugField(max_length=200, unique=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    # French (required)
    name_fr = models.CharField(max_length=200, verbose_name="Nom (FR)")
    title_fr = models.CharField(max_length=300, verbose_name="Titre (FR)")
    content_fr = models.TextField(verbose_name="Contenu (FR)")
    meta_description_fr = models.CharField(max_length=160, blank=True, verbose_name="Meta Description (FR)")

    # English
    name_en = models.CharField(max_length=200, blank=True)
    title_en = models.CharField(max_length=300, blank=True)
    content_en = models.TextField(blank=True)
    meta_description_en = models.CharField(max_length=160, blank=True)

    # Arabic
    name_ar = models.CharField(max_length=200, blank=True)
    title_ar = models.CharField(max_length=300, blank=True)
    content_ar = models.TextField(blank=True)
    meta_description_ar = models.CharField(max_length=160, blank=True)

    class Meta:
        verbose_name = "Neighborhood Page"
        verbose_name_plural = "Neighborhood Pages"
        ordering = ['name_fr']

    def __str__(self):
        return self.name_fr

    def get_name(self, lang=None):
        from django.utils import translation
        if not lang:
            lang = translation.get_language() or 'fr'
        return getattr(self, f'name_{lang}', '') or self.name_fr

    def get_title(self, lang=None):
        from django.utils import translation
        if not lang:
            lang = translation.get_language() or 'fr'
        return getattr(self, f'title_{lang}', '') or self.title_fr

    def get_content(self, lang=None):
        from django.utils import translation
        if not lang:
            lang = translation.get_language() or 'fr'
        return getattr(self, f'content_{lang}', '') or self.content_fr

    def get_meta_description(self, lang=None):
        from django.utils import translation
        if not lang:
            lang = translation.get_language() or 'fr'
        return getattr(self, f'meta_description_{lang}', '') or self.get_title(lang)[:160]

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('core:neighborhood_detail', kwargs={'slug': self.slug})
