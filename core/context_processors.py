"""
Context processors for Laboratoire International.
Reads from SiteSettings (DB) and provides site-wide variables to all templates.
"""
from django.conf import settings
from django.utils.translation import get_language, gettext as _


def site_context(request):
    """Inject site-wide variables into template context from SiteSettings DB model."""
    from .models import SiteSettings

    current_lang = get_language() or 'fr'
    is_rtl = current_lang == 'ar'

    # Load site settings from DB (cached)
    try:
        site = SiteSettings.load()
    except Exception:
        site = None

    # Language flag codes for flagcdn.com
    lang_flag_codes = {
        'fr': 'fr',
        'en': 'gb',
        'ar': 'ma',
        'nl': 'nl',
        'de': 'de',
        'es': 'es',
        'it': 'it',
    }
    current_flag_code = lang_flag_codes.get(current_lang, 'fr')

    if site:
        # Read everything from DB
        social_links = site.get_social_links()
        social_urls = [link['url'] for link in social_links if link['name'] != 'WhatsApp']

        return {
            'SITE_NAME': _(site.site_name),
            'SITE_SLOGAN': site.get_slogan(current_lang),
            'SITE_DOMAIN': getattr(settings, 'SITE_DOMAIN', site.site_domain),
            'SITE_PHONE': site.phone,
            'SITE_EMAIL': getattr(settings, 'SITE_EMAIL', site.email),
            'SITE_WHATSAPP': site.whatsapp,
            'SITE_ADDRESS': site.address,
            'SITE_MAPS_URL': site.maps_url,
            'SITE_MAPS_EMBED': site.maps_embed,
            'VISIONLIS_URL': site.visionlis_url,
            'GA4_MEASUREMENT_ID': site.ga4_measurement_id,
            'OPENING_HOURS': site.opening_hours,
            'OPENING_DAYS': site.get_opening_days(current_lang),
            'CLOSED_DAY': site.get_closed_day(current_lang),
            'SOCIAL_LINKS': social_links,
            'SOCIAL_URLS_JSON': social_urls,
            'FACEBOOK_URL': site.facebook_url,
            'INSTAGRAM_URL': site.instagram_url,
            'LINKEDIN_URL': site.linkedin_url,
            'CURRENT_LANG': current_lang,
            'IS_RTL': is_rtl,
            'LANGUAGES': getattr(settings, 'LANGUAGES', []),
            'CURRENT_FLAG_CODE': current_flag_code,
        }
    else:
        # Fallback to settings.py (before first DB setup)
        site_slogan_map = {
            'fr': 'Analyses Médicales',
            'en': 'Medical Laboratory',
            'ar': 'مختبر التحاليل الطبية',
            'es': 'Laboratorio de Análisis Médicos',
            'de': 'Medizinisches Labor',
            'nl': 'Medisch Laboratorium',
            'it': 'Laboratorio di Analisi Mediche',
        }

        return {
            'SITE_NAME': _('Laboratoire International Tanger'),
            'SITE_SLOGAN': site_slogan_map.get(current_lang, _('Analyses Médicales')),
            'SITE_DOMAIN': getattr(settings, 'SITE_DOMAIN', 'laboratoiretanger.com'),
            'SITE_PHONE': getattr(settings, 'SITE_PHONE', '+212 5 39 31 39 47'),
            'SITE_EMAIL': getattr(settings, 'SITE_EMAIL', 'contact@laboratoiretanger.com'),
            'SITE_WHATSAPP': '212539313947',
            'SITE_ADDRESS': getattr(settings, 'SITE_ADDRESS', 'Avenue Moulay Rachid, Tanger 90000, Morocco'),
            'SITE_MAPS_URL': getattr(settings, 'SITE_MAPS_URL', ''),
            'SITE_MAPS_EMBED': getattr(settings, 'SITE_MAPS_EMBED', ''),
            'VISIONLIS_URL': getattr(settings, 'VISIONLIS_URL', ''),
            'GA4_MEASUREMENT_ID': getattr(settings, 'GA4_MEASUREMENT_ID', ''),
            'OPENING_HOURS': '',
            'OPENING_DAYS': 'Lundi - Vendredi : 07:00 - 19:00 | Samedi : 07:00 - 15:00',
            'CLOSED_DAY': 'Dimanche: Fermé',
            'SOCIAL_LINKS': [],
            'SOCIAL_URLS_JSON': [],
            'FACEBOOK_URL': '',
            'INSTAGRAM_URL': '',
            'LINKEDIN_URL': '',
            'CURRENT_LANG': current_lang,
            'IS_RTL': is_rtl,
            'LANGUAGES': getattr(settings, 'LANGUAGES', []),
            'CURRENT_FLAG_CODE': current_flag_code,
        }
