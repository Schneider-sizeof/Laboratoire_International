"""
Django settings for labinternational project.
Laboratoire International d'Analyses Médicales — Tangier, Morocco
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# ============================================================
# Security
# ============================================================
SECRET_KEY = os.environ.get(
    'SECRET_KEY',
    'django-insecure-#bj%f7j5erhb&=_(gie!(^kv0w8)(m6ghvq=$97jdg_f-ujiv1'
)

DEBUG = os.environ.get('DEBUG', 'True').lower() in ('true', '1', 'yes')

ALLOWED_HOSTS = os.environ.get(
    'ALLOWED_HOSTS',
    'laboratoireinternational.pythonanywhere.com,schneider-sizeof.pythonanywhere.com,laboratoireinternational.com,localhost,127.0.0.1'
).split(',')


# ============================================================
# Application definition
# ============================================================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'core',
]

MIDDLEWARE = [
    'core.middleware.LicenseVerificationMiddleware',   # Anti-piracy Gist check
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',       # i18n language detection
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'labinternational.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'core.context_processors.site_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'labinternational.wsgi.application'


# ============================================================
# Database
# ============================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ============================================================
# Password validation
# ============================================================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# ============================================================
# Internationalization (i18n)
# ============================================================
LANGUAGE_CODE = 'fr'

LANGUAGES = [
    ('fr', 'Français'),
    ('en', 'English'),
    ('ar', 'العربية'),
    ('nl', 'Nederlands'),
    ('de', 'Deutsch'),
    ('es', 'Español'),
]

TIME_ZONE = 'Africa/Casablanca'

USE_I18N = True
USE_L10N = True
USE_TZ = True

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

LANGUAGE_COOKIE_NAME = 'lab_lang'
LANGUAGE_COOKIE_AGE = 365 * 24 * 60 * 60  # 1 year


# ============================================================
# Static & Media files
# ============================================================
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = []

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# ============================================================
# Default primary key field type
# ============================================================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ============================================================
# Email (for contact form)
# ============================================================
EMAIL_BACKEND = os.environ.get(
    'EMAIL_BACKEND', 'django.core.mail.backends.console.EmailBackend'
)
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT', '587'))
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', 'True').lower() in ('true', '1')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')


# ============================================================
# Site-specific settings
# ============================================================
SITE_NAME = "Laboratoire International"
SITE_SLOGAN = "Votre santé est Notre propriété"
SITE_DOMAIN = "laboratoireinternational.com"
SITE_PHONE = "+212 5 39 31 39 47"
SITE_EMAIL = "contact@laboratoireinternational.com"
SITE_ADDRESS = "Avenue Moulay Rachid, Tanger 90000, Morocco"
SITE_MAPS_URL = "https://maps.app.goo.gl/HSkgrJB5ffH6xe727"
SITE_MAPS_EMBED = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3237.922853199904!2d-5.853466!3d35.7527009!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xd0b87bb4130edf5%3A0xb2bc80cfeb3a4755!2sLaboratoire%20International!5e0!3m2!1sen!2sma!4v1"
VISIONLIS_URL = os.environ.get(
    'VISIONLIS_URL', 'http://liamt.ddns.net:12543/visionlis/#/loginpatient'
)
GA4_MEASUREMENT_ID = os.environ.get('GA4_MEASUREMENT_ID', '')

# ============================================================
# Licensing Configuration
# ============================================================
LICENSE_GIST_URL = os.environ.get('LICENSE_GIST_URL')
LICENSE_KEY = os.environ.get('LICENSE_KEY', 'CM2026X')

