"""
Django settings for Study_Swamp_BE project.

See:
- https://docs.djangoproject.com/en/4.1/topics/settings/
- https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path

# ---------------------------------------------------------
# BASE DIRECTORIES
# ---------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent


# ---------------------------------------------------------
# SECURITY
# ---------------------------------------------------------

# SECURITY WARNING:
# keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-s@27u^(*bj8)f4(a-suj^itcynrtjqy73#up$^+!d#^l#qs*f$'

# SECURITY WARNING:
# don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# ---------------------------------------------------------
# APPLICATION DEFINITION
# ---------------------------------------------------------

INSTALLED_APPS = [
    # Your app
    'Study_Swamp_API',

    # Third-party
    'rest_framework',
    'corsheaders',

    # Django built-in
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Allow CORS for APIs
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Allow all origins during dev; restrict in production!
CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'Study_Swamp_BE.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Add template paths if you have them
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Study_Swamp_BE.wsgi.application'


# ---------------------------------------------------------
# DATABASE CONFIGURATION
# ---------------------------------------------------------

# Uses environment variables for flexibility across environments (local, Docker, CI)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('POSTGRES_DB', 'study_swamp_db'),
        'USER': os.getenv('POSTGRES_USER', 'hero'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'password'),
        'HOST': os.getenv('POSTGRES_HOST', 'localhost'),
        'PORT': os.getenv('POSTGRES_PORT', '5432'),
        'TEST': {
            'NAME': 'test_study_swamp_db',
        },
    }
}


# ---------------------------------------------------------
# PASSWORD VALIDATION
# ---------------------------------------------------------

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


# ---------------------------------------------------------
# INTERNATIONALIZATION
# ---------------------------------------------------------

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# ---------------------------------------------------------
# STATIC FILES
# ---------------------------------------------------------

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# ---------------------------------------------------------
# DEFAULT PRIMARY KEY FIELD TYPE
# ---------------------------------------------------------

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ---------------------------------------------------------
# CUSTOM USER MODEL
# ---------------------------------------------------------

# Tells Django to use your custom user model
AUTH_USER_MODEL = 'Study_Swamp_API.User'


# ---------------------------------------------------------
# DJANGO REST FRAMEWORK SETTINGS
# ---------------------------------------------------------

REST_FRAMEWORK = {
    # JSON:API exception formatting
    'EXCEPTION_HANDLER': 'rest_framework_json_api.exceptions.exception_handler',

    # JSON:API pagination
    'DEFAULT_PAGINATION_CLASS': 'rest_framework_json_api.pagination.JsonApiPageNumberPagination',

    # Parsers for JSON:API, JSON, and forms
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework_json_api.parsers.JSONParser',
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ),

    # Authentication mechanisms:
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',  # Optional browser login
    ],

    # Default permissions: require authentication
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],

    # Renderers for JSON:API and Browsable API
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework_json_api.renderers.JSONRenderer',
        # Uncomment if you want a browsable API without forms for perf:
        # 'example.utils.BrowsableAPIRendererWithoutForms',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),

    # JSON:API-specific configuration
    'DEFAULT_METADATA_CLASS': 'rest_framework_json_api.metadata.JSONAPIMetadata',

    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework_json_api.filters.QueryParameterValidationFilter',
        'rest_framework_json_api.filters.OrderingFilter',
        'rest_framework_json_api.django_filters.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
    ),

    'SEARCH_PARAM': 'filter[search]',

    # JSON:API for tests
    'TEST_REQUEST_RENDERER_CLASSES': (
        'rest_framework_json_api.renderers.JSONRenderer',
    ),
    'TEST_REQUEST_DEFAULT_FORMAT': 'vnd.api+json'
}
