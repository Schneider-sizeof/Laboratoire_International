"""
Django admin configuration for Laboratoire International.
"""
from django.contrib import admin
from .models import BlogCategory, BlogPost, ContactSubmission


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('name_fr', 'slug', 'order', 'created_at')
    prepopulated_fields = {'slug': ('name_fr',)}
    ordering = ('order',)


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
    )

    def publish_posts(self, request, queryset):
        from django.utils import timezone
        queryset.update(status='published', published_at=timezone.now())
    publish_posts.short_description = "Publish selected posts"

    def unpublish_posts(self, request, queryset):
        queryset.update(status='draft')
    unpublish_posts.short_description = "Unpublish selected posts"


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
