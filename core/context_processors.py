"""
Context processors for Laboratoire International.
Provides site-wide variables to all templates.
"""
from django.conf import settings
from django.utils.translation import get_language, gettext as _


def site_context(request):
    """Inject site-wide variables into template context."""
    current_lang = get_language() or 'fr'
    is_rtl = current_lang == 'ar'

    lang_flags = {
        'fr': '🇫🇷',
        'en': '🇬🇧',
        'ar': '🇲🇦',
        'nl': '🇳🇱',
        'de': '🇩🇪',
        'es': '🇪🇸',
    }
    current_flag = lang_flags.get(current_lang, '🇫🇷')

    lang_flag_codes = {
        'fr': 'fr',
        'en': 'gb',
        'ar': 'ma',
        'nl': 'nl',
        'de': 'de',
        'es': 'es',
    }
    current_flag_code = lang_flag_codes.get(current_lang, 'fr')

    # Translate the site name – French is the default (msgid)
    site_name = _('Laboratoire International')

    # Translate the subtitle shown under the brand
    site_slogan_map = {
        'fr': 'Analyses Médicales',
        'en': 'Medical Laboratory',
        'ar': 'مختبر التحاليل الطبية',
        'es': 'Laboratorio de Análisis Médicos',
        'de': 'Medizinisches Labor',
        'nl': 'Medisch Laboratorium',
    }
    site_slogan = site_slogan_map.get(current_lang, _('Analyses Médicales'))

    return {
        'SITE_NAME': site_name,
        'SITE_SLOGAN': site_slogan,
        'SITE_DOMAIN': getattr(settings, 'SITE_DOMAIN', 'laboratoireinternational.com'),
        'SITE_PHONE': getattr(settings, 'SITE_PHONE', '+212 5 39 31 39 47'),
        'SITE_EMAIL': getattr(settings, 'SITE_EMAIL', 'contact@laboratoireinternational.com'),
        'SITE_ADDRESS': getattr(settings, 'SITE_ADDRESS', 'Avenue Moulay Rachid, Tanger 90000, Morocco'),
        'SITE_MAPS_URL': getattr(settings, 'SITE_MAPS_URL', ''),
        'SITE_MAPS_EMBED': getattr(settings, 'SITE_MAPS_EMBED', ''),
        'VISIONLIS_URL': getattr(settings, 'VISIONLIS_URL', ''),
        'GA4_MEASUREMENT_ID': getattr(settings, 'GA4_MEASUREMENT_ID', ''),
        'CURRENT_LANG': current_lang,
        'IS_RTL': is_rtl,
        'LANGUAGES': getattr(settings, 'LANGUAGES', []),
        'CURRENT_FLAG': current_flag,
        'CURRENT_FLAG_CODE': current_flag_code,
    }
