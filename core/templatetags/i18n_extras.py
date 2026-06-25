from django import template
from django.urls import translate_url as django_translate_url

register = template.Library()

@register.simple_tag(takes_context=True)
def translate_url(context, lang_code):
    """
    Template tag to translate the current request URL into another language.
    Usage: {% translate_url 'en' %}
    """
    request = context.get('request')
    if not request:
        return ''
    return django_translate_url(request.get_full_path(), lang_code)
