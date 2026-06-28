"""
Django settings for labinternational project.
Laboratoire International d'Analyses Médicales — Tangier, Morocco
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Load .env file manually if it exists (zero external dependencies)
env_file = BASE_DIR / '.env'
if env_file.exists():
    with open(env_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if '=' in line:
                key, val = line.split('=', 1)
                key = key.strip()
                val = val.strip().strip("'\"")
                os.environ[key] = val


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
    'laboratoiretanger.com,www.laboratoiretanger.com,laboratoireinternational.com,www.laboratoireinternational.com,schneider-sizeof.pythonanywhere.com,localhost,127.0.0.1'
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
    'core.middleware.DomainRedirectMiddleware',
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
    ('it', 'Italiano'),
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
# Email (fallback — actual config in SiteSettings admin)
# ============================================================
EMAIL_BACKEND = os.environ.get(
    'EMAIL_BACKEND', 'django.core.mail.backends.console.EmailBackend'
)


# ============================================================
# Site-specific settings (fallback for context_processors)
# ============================================================
SITE_NAME = "Laboratoire International Tanger"
SITE_SLOGAN = "Votre santé est Notre priorité"
SITE_DOMAIN = "laboratoiretanger.com"
SITE_PHONE = "+212 5 39 31 39 47"
SITE_EMAIL = "contact@laboratoiretanger.com"
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


# ============================================================
# Production Security (applied when DEBUG=False)
# ============================================================
if not DEBUG:
    # HTTPS
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

    # HSTS
    SECURE_HSTS_SECONDS = 31536000  # 1 year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

    # Security headers
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    X_FRAME_OPTIONS = 'DENY'

    # CSRF
    CSRF_TRUSTED_ORIGINS = [
        'https://laboratoiretanger.com',
        'https://www.laboratoiretanger.com',
    ]

    # Logging
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': '{levelname} {asctime} {module} {message}',
                'style': '{',
            },
        },
        'handlers': {
            'file': {
                'level': 'ERROR',
                'class': 'logging.FileHandler',
                'filename': BASE_DIR / 'logs' / 'django_errors.log',
                'formatter': 'verbose',
            },
        },
        'root': {
            'handlers': ['file'],
            'level': 'ERROR',
        },
    }
