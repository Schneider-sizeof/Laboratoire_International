"""
URL configuration for labinternational project.
Uses i18n_patterns for automatic language prefix routing.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.contrib.sitemaps.views import sitemap

from core.sitemaps import StaticSitemap, BlogSitemap
from core.views import robots_txt

sitemaps = {
    'static': StaticSitemap,
    'blog': BlogSitemap,
}

# Non-i18n URLs (no language prefix)
urlpatterns = [
    path('robots.txt', robots_txt, name='robots_txt'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('i18n/', include('django.conf.urls.i18n')),
]

# i18n URLs (with language prefix: /fr/, /en/, /ar/, etc.)
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    prefix_default_language=True,
)

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
