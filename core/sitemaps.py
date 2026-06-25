"""
Sitemap configuration for SEO.
"""
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import BlogPost, Analysis, NeighborhoodPage


class StaticSitemap(Sitemap):
    """Sitemap for static pages."""
    changefreq = 'weekly'
    protocol = 'https'

    def items(self):
        return [
            'core:home',
            'core:about',
            'core:services',
            'core:results',
            'core:blog_list',
            'core:contact',
            'core:legal_privacy',
            'core:legal_terms',
            'core:legal_cookies',
        ]

    def location(self, item):
        return reverse(item)

    def priority(self, item):
        priorities = {
            'core:home': 1.0,
            'core:services': 0.9,
            'core:contact': 0.8,
            'core:about': 0.8,
            'core:results': 0.7,
            'core:blog_list': 0.7,
        }
        return priorities.get(item, 0.5)


class BlogSitemap(Sitemap):
    """Sitemap for published blog posts."""
    changefreq = 'monthly'
    priority = 0.6
    protocol = 'https'

    def items(self):
        return BlogPost.objects.filter(status='published')

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return reverse('core:blog_detail', kwargs={'slug': obj.slug})


class AnalysisSitemap(Sitemap):
    """Sitemap for individual analysis pages."""
    changefreq = 'monthly'
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Analysis.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return reverse('core:analysis_detail', kwargs={'slug': obj.slug})


class NeighborhoodSitemap(Sitemap):
    """Sitemap for neighborhood pages."""
    changefreq = 'monthly'
    priority = 0.7
    protocol = 'https'

    def items(self):
        return NeighborhoodPage.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return reverse('core:neighborhood_detail', kwargs={'slug': obj.slug})
