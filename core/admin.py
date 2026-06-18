"""
Django admin configuration for Laboratoire International.
Rich admin panel with SiteSettings, Team, Partners, Blog, and Contacts.
"""
from django.contrib import admin
from django.utils.html import format_html
from .models import SiteSettings, TeamMember, Partner, BlogCategory, BlogPost, ContactSubmission


# ============================================================
# Site Settings (Singleton Admin)
# ============================================================
@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    """Single-page admin for all site configuration."""

    fieldsets = (
        ('🏢 Informations Générales', {
            'fields': ('site_name', 'site_domain'),
        }),
        ('📝 Slogan / Tagline', {
            'fields': (
                'site_slogan_fr', 'site_slogan_en', 'site_slogan_ar',
                'site_slogan_es', 'site_slogan_de', 'site_slogan_nl', 'site_slogan_it',
            ),
        }),
        ('📞 Contact', {
            'fields': ('phone', 'email', 'whatsapp', 'address', 'maps_url', 'maps_embed'),
        }),
        ('🕐 Horaires d\'ouverture', {
            'fields': (
                'opening_hours',
                'opening_days_fr', 'opening_days_en', 'opening_days_ar',
                'closed_day_fr', 'closed_day_en', 'closed_day_ar',
            ),
        }),
        ('🌐 Réseaux Sociaux', {
            'fields': ('facebook_url', 'instagram_url', 'linkedin_url', 'youtube_url', 'tiktok_url'),
        }),
        ('📊 Google Analytics', {
            'fields': ('ga4_measurement_id',),
        }),
        ('🔬 VisionLIS', {
            'fields': ('visionlis_url',),
        }),
        ('📧 Email Notifications (Contact Form)', {
            'fields': ('notification_email', 'smtp_host', 'smtp_port', 'smtp_user', 'smtp_password', 'smtp_use_tls'),
            'description': 'Configurez l\'envoi d\'emails pour les soumissions du formulaire de contact.',
        }),
    )

    def has_add_permission(self, request):
        # Only allow one instance
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        # Redirect to the single instance edit page
        obj, created = SiteSettings.objects.get_or_create(pk=1)
        from django.shortcuts import redirect
        return redirect(f'/admin/core/sitesettings/{obj.pk}/change/')


# ============================================================
# Team Members
# ============================================================
@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role_fr', 'order', 'photo_preview', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'role_fr')
    ordering = ('order',)

    fieldsets = (
        ('👤 Identité', {
            'fields': ('name', 'initials', 'photo', 'order', 'is_active'),
        }),
        ('🇫🇷 Français', {
            'fields': ('role_fr', 'bio_fr'),
        }),
        ('🇬🇧 English', {
            'classes': ('collapse',),
            'fields': ('role_en', 'bio_en'),
        }),
        ('🇲🇦 العربية', {
            'classes': ('collapse',),
            'fields': ('role_ar', 'bio_ar'),
        }),
        ('🇪🇸 Español', {
            'classes': ('collapse',),
            'fields': ('role_es', 'bio_es'),
        }),
        ('🇩🇪 Deutsch', {
            'classes': ('collapse',),
            'fields': ('role_de', 'bio_de'),
        }),
        ('🇳🇱 Nederlands', {
            'classes': ('collapse',),
            'fields': ('role_nl', 'bio_nl'),
        }),
        ('🇮🇹 Italiano', {
            'classes': ('collapse',),
            'fields': ('role_it', 'bio_it'),
        }),
    )

    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="40" height="40" style="border-radius:50%;object-fit:cover;" />', obj.photo.url)
        return format_html('<span style="display:inline-flex;align-items:center;justify-content:center;width:40px;height:40px;border-radius:50%;background:#e3f2fd;color:#1976d2;font-weight:bold;">{}</span>', obj.initials)
    photo_preview.short_description = 'Photo'


# ============================================================
# Partners
# ============================================================
@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo_preview', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)
    ordering = ('order',)

    fieldsets = (
        ('🤝 Partenaire', {
            'fields': ('name', 'logo', 'icon', 'url', 'order', 'is_active'),
        }),
        ('🇫🇷 Français', {
            'fields': ('description_fr',),
        }),
        ('🇬🇧 English', {
            'classes': ('collapse',),
            'fields': ('description_en',),
        }),
        ('🇲🇦 العربية', {
            'classes': ('collapse',),
            'fields': ('description_ar',),
        }),
        ('🇪🇸 Español', {
            'classes': ('collapse',),
            'fields': ('description_es',),
        }),
        ('🇩🇪 Deutsch', {
            'classes': ('collapse',),
            'fields': ('description_de',),
        }),
        ('🇳🇱 Nederlands', {
            'classes': ('collapse',),
            'fields': ('description_nl',),
        }),
        ('🇮🇹 Italiano', {
            'classes': ('collapse',),
            'fields': ('description_it',),
        }),
    )

    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" width="60" height="30" style="object-fit:contain;" />', obj.logo.url)
        if obj.icon:
            return format_html('<i class="{}"></i>', obj.icon)
        return '-'
    logo_preview.short_description = 'Logo'


# ============================================================
# Blog Category
# ============================================================
@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('name_fr', 'slug', 'order', 'created_at')
    prepopulated_fields = {'slug': ('name_fr',)}
    ordering = ('order',)


# ============================================================
# Blog Post
# ============================================================
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title_fr', 'category', 'status', 'author', 'is_featured', 'views_count', 'published_at')
    list_filter = ('status', 'category', 'is_featured', 'created_at')
    search_fields = ('title_fr', 'title_en', 'content_fr', 'content_en', 'tags')
    prepopulated_fields = {'slug': ('title_fr',)}
    date_hierarchy = 'created_at'
    readonly_fields = ('views_count', 'created_at', 'updated_at')
    actions = ['publish_posts', 'unpublish_posts']

    fieldsets = (
        ('Status & Metadata', {
            'fields': ('slug', 'status', 'category', 'featured_image', 'author', 'tags',
                       'is_featured', 'published_at', 'views_count', 'created_at', 'updated_at'),
        }),
        ('🇫🇷 Français (default)', {
            'fields': ('title_fr', 'excerpt_fr', 'content_fr', 'meta_title_fr', 'meta_description_fr'),
        }),
        ('🇬🇧 English', {
            'classes': ('collapse',),
            'fields': ('title_en', 'excerpt_en', 'content_en', 'meta_title_en', 'meta_description_en'),
        }),
        ('🇲🇦 العربية', {
            'classes': ('collapse',),
            'fields': ('title_ar', 'excerpt_ar', 'content_ar', 'meta_title_ar', 'meta_description_ar'),
        }),
        ('🇳🇱 Nederlands', {
            'classes': ('collapse',),
            'fields': ('title_nl', 'excerpt_nl', 'content_nl', 'meta_title_nl', 'meta_description_nl'),
        }),
        ('🇩🇪 Deutsch', {
            'classes': ('collapse',),
            'fields': ('title_de', 'excerpt_de', 'content_de', 'meta_title_de', 'meta_description_de'),
        }),
        ('🇪🇸 Español', {
            'classes': ('collapse',),
            'fields': ('title_es', 'excerpt_es', 'content_es', 'meta_title_es', 'meta_description_es'),
        }),
        ('🇮🇹 Italiano', {
            'classes': ('collapse',),
            'fields': ('title_it', 'excerpt_it', 'content_it', 'meta_title_it', 'meta_description_it'),
        }),
    )

    def publish_posts(self, request, queryset):
        from django.utils import timezone
        queryset.update(status='published', published_at=timezone.now())
    publish_posts.short_description = "Publish selected posts"

    def unpublish_posts(self, request, queryset):
        queryset.update(status='draft')
    unpublish_posts.short_description = "Unpublish selected posts"


# ============================================================
# Contact Submissions
# ============================================================
@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'service_type', 'is_read', 'created_at')
    list_filter = ('service_type', 'is_read', 'created_at')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('name', 'email', 'phone', 'service_type', 'message', 'created_at')
    date_hierarchy = 'created_at'
    actions = ['mark_as_read', 'mark_as_unread']

    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Mark as read"

    def mark_as_unread(self, request, queryset):
        queryset.update(is_read=False)
    mark_as_unread.short_description = "Mark as unread"


# ============================================================
# Admin Site Customization
# ============================================================
admin.site.site_header = "Laboratoire International — Administration"
admin.site.site_title = "LIAM Admin"
admin.site.index_title = "Gestion du site"
