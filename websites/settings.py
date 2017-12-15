"""
Django settings for metiz project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2+@8!9c)(s11nt^ox20nkvu7)_wqh6=g(p54jlsjytizbuz(4y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'main',
    'core',
    'registration',
    'booking',
    # 'core.apps.CoreConfig',
    'ckeditor',
    'ckeditor_uploader',
    'captcha',
    # 'allauth',
    # 'allauth.account',
    # 'allauth.socialaccount',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'booking.middleware.DestroySeat',
]

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                # 'allauth.account.context_processors.account',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.static',
                'django.template.context_processors.media',
                'django.template.context_processors.i18n',
                'main.context_processors.get_app_fb_id',
                'main.context_processors.get_app_recaptcha_key',
            ],
        },
    },
]

WSGI_APPLICATION = 'main.wsgi.application'


# Custom User Model
AUTH_USER_MODEL = 'core.User'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    # 'allauth.account.auth_backends.AuthenticationBackend',
)


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

# config model translation
gettext = lambda s: s
LANGUAGES = (
    ('vi', gettext('Vietnamese')),
    ('en-us', gettext('English')),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

LANGUAGE_CODE = 'vi'

TIME_ZONE = 'Asia/Saigon'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'public/static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'public', 'media')

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, "static"),
)

# Config CK_Editor
CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'extraPlugins': ','.join(
            [
               'codesnippetgeshi',
               'placeholder',
               'dialog',
               'dialogui',
               'embed',
            ]
        ),
        'font_names': "Yanone Kaffeesatz; Cabin",
        'contentsCss': ','.join(['/static/assets/websites/css/custom_admin.css']),
        'allowedContent': True
    },
}
CKEDITOR_BROWSE_SHOW_DIRS = True
CKEDITOR_IMAGE_BACKEND = "pillow"

# Config outgoing email
EMAIL_BACKEND = "main.email_backend.DKIMBackend"
DEFAULT_TO_ADMIN_EMAIL = "contact@metiz.vn"
DEFAULT_FROM_EMAIL = "no-reply@metiz.vn"
# EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
EMAIL_HOST = 'mail.helio.vn'
EMAIL_HOST_USER = 'no-reply@helio.vn'
EMAIL_HOST_PASSWORD = 'N0reply!@#'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Config DKIM
DKIM_SELECTOR = "metiz_dkim"
DKIM_DOMAIN = "metiz.vn"
DKIM_PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIICXQIBAAKBgQC1jD/O9VRWvwqeEnxnSGrhh7BYqaGMGn94i48yMBvVc7XfT7eC
5J1Cf/iV0NRwe4EJiRm62VF56TJcl050HunKtVisgFOuT6qWLbceKL5/+PAumag0
HrUdw3Vm89qRyNJrwLNtUkgBC1rvcuWvRTSmMukQCPaPG1KoI7eEg79YBQIDAQAB
AoGBAIbB0eNHCxFQwQrQYfMwN9WsKGPHlhgu2wuZW/M+7ookV42o2GiaVXi1EMnz
tpy/r+pqD+U3xlidljpQPXXINHR4qgX0SdwgqLnItiDhTqwI71X7Hi+JI4LWUkav
HZL96OwzIeJKvkZfAkujOj+Ep3BLKmnv6SBkn/t0HUFKGscJAkEA3uhcP30Lri6p
VByuPZZlY2IzQ3P5yyTkaPFTNuPWO5RZKls31pZ3Q8VPGjRHD17cF/+RBXfr1ECX
xM6BEUw5dwJBANCAAMb4YFS7LZ+6BmBtwwoHHAEGMB7mtU6+O6mo2NBhyz+Y0INt
KW1GvOnzCYMQCltv79nEleFtscAVfs27mWMCQCOlJJtCc8u2yn0Y2QQgOLZbzbbL
pPZHP/9IF/Z/GJMOdfPAAn3eMdQ0iSG3mmVq1edAhwBI3P1kFuDx5NHPTqECQQCI
Bwr6xO7sONYyQEaKwPGfaDYAAQ6CCpi9T+VS8iLKCRN2YXegVybQ8Xas13AcPunS
7/u2wsfaNBvkquF4zezrAkBvCJfeZMr2oiXsw8P3dGkSkGs9BkJetAdtzVn7VjF4
Eq/hPY3tgE5GI/V4OPczdJP6hoG1uynU2SKbKMJ2rAJz
-----END RSA PRIVATE KEY-----"""

# HERE FORMATING AS shown in:
# LIST: https://docs.djangoproject.com/en/dev/ref/templates/builtins/#date
DATE_FORMAT = 'd-m-Y'
TIME_FORMAT = 'H:i'
DATETIME_FORMAT = 'd-m-Y H:i'
YEAR_MONTH_FORMAT = 'F Y'
MONTH_DAY_FORMAT = 'F j'
SHORT_DATE_FORMAT = 'm/d/Y'
SHORT_DATETIME_FORMAT = 'm/d/Y P'
FIRST_DAY_OF_WEEK = 1

# BUT here use the Python strftime format syntax,
# LIST: http://docs.python.org/library/datetime.html#strftime-strptime-behavior

DATE_INPUT_FORMATS = (
    '%d-%m-%Y',     # '21-03-2014'
)
TIME_INPUT_FORMATS = (
    '%H:%M:%S',     # '17:59:59'
    '%H:%M',        # '17:59'
)
DATETIME_INPUT_FORMATS = (
    '%d-%m-%Y %H:%M',     # '21-03-2014 17:59'
)

DECIMAL_SEPARATOR = u'.'
THOUSAND_SEPARATOR = u','
NUMBER_GROUPING = 3

# # Config Django Allauth
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_AUTHENTICATION_METHOD = 'email'
# ACCOUNT_UNIQUE_EMAIL = True
# ACCOUNT_USERNAME_REQUIRED = False
# ACCOUNT_USER_MODEL_USERNAME_FIELD = None
LOGIN_REDIRECT_URL = '/'
LOGIN_URL='/'

# Set timeout for choice seats
TIME_SEAT_DELAY = 5

# Config Google reCaptcha
NOCAPTCHA = True

try:
    if 'DEVELOPMENT' in os.environ and os.environ['DEVELOPMENT']:
        from config.setting_develop import *
    elif 'UAT' in os.environ and os.environ['UAT']:
        from config.setting_uat import *
    elif 'PRODUCTION' in os.environ and os.environ['PRODUCTION']:
        from config.setting_production import *
    else:
        from config.setting_local import *
    
except ImportError:
    pass

