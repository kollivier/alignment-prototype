"""
Django settings for alignmentpro project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "uzg!6^y3pio6*^c5xjewtq(hdigl*q#q5s9b6^@c1-40v+y2k9"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "treebeard",  # for TreeAdmin views
    "alignmentapp",
    "corsheaders",
    "commonstandardsproject",  # tmp to extract CCSS and NGSS data
    "importing",
    "django_extensions",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "alignmentpro.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "alignmentpro.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "alignmentpro",
        "USER": "",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": "",
    },
    "standards": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "standards",
        "USER": "",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": "",
    },
}

DATABASE_ROUTERS = ["alignmentpro.dbrouters.DbRouter"]


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = "/static/"


REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly"
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 20,
}


# Data export paths and constnts
DATA_EXPORT_BASE_DIR = os.path.join(BASE_DIR, "..", "exports", "data")
CURRICULUM_DOCUMENTS_FILENAME = "curriculumdocuments.csv"
STANDARD_NODES_FILENAME = "standardnodes.csv"
HUMAN_JUDGMENTS_FILENAME = "humanjudgments.csv"
HUMAN_JUDGMENTS_TEST_FILENAME = "humanjudgments_test.csv"
METADATA_FILENAME = "metadata.json"

# in production, we'd want to limit this, but for hackathon purposes
# we want to make sure everyone doing local dev can reach the API.
# TODO: switch to whitelist once in production, via instructions at:
# https://pypi.org/project/django-cors-headers/
CORS_ORIGIN_ALLOW_ALL = True
