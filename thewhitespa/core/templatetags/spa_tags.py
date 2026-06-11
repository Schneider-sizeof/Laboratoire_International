from django import template

register = template.Library()

CATEGORY_IMAGES = {
    'HAMMAM': 'core/images/hammam.png',
    'MASSAGE': 'core/images/massage.png',
    'FACIAL': 'core/images/facial.png',
    'BODY': 'core/images/massage.png',
    'PACKAGE': 'core/images/hero.png',
}

@register.simple_tag
def service_image(service):
    """Return the static path for a service based on its category."""
    return CATEGORY_IMAGES.get(service.category, 'core/images/hero.png')
