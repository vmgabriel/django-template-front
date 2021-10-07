"""Settings"""

# Libraries
import os
import sys
import environ
import django_heroku
from pathlib import Path
from datetime import timedelta
from .app import MDA_APPS

env = environ.Env()
BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

SECRET_KEY = env("SECRET_KEY")
MODE = (env("MODE", default="production")).lower()
DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", 't')


ALLOWED_HOSTS = ["127.0.0.1", "*.herokuapp.com"]


USER_APPLICATIONS = [
    "core",
    "pages.apps.PagesConfig",
    "accounts.apps.AccountsConfig",
] + MDA_APPS
EXTERNAL_APPLICATIONS = [
    "versatileimagefield",
    "django_sass",
    "django_filters",
]
INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
] + EXTERNAL_APPLICATIONS + USER_APPLICATIONS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

WSGI_APPLICATION = "config.wsgi.application"


DATABASES = {
    "default": env.db(),
    "extra": env.db("SQLITE_URL", default="sqlite:////tmp/my_db.sqlite3"),
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTH_USER_MODEL = "accounts.User"
LOGIN_REDIRECT_URL = "pages:home"
LOGOUT_REDIRECT_URL = "pages:home"

# Server Configuration
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static Configuration of Server
STATIC_URL = "/static/"
# STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = (
  os.path.join(BASE_DIR, "static/"),
)

# DB Configuration
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Email Configuration
SEND_EMAIL = False
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")

# Paginations of page
DEFAULT_COUNT_PAGINATE = 20


WHITENOISE_USE_FINDERS = True
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

if MODE == "production":
    django_heroku.settings(locals())
