
"""
Django settings for config project.
"""

import os
from pathlib import Path
from datetime import timedelta

from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# Rutas del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Seguridad
SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = os.environ.get("DEBUG", "False").lower() == "true"
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# Aplicaciones instaladas
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "core",
    "Autos",
    "Precios",
]

# Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# URLs principales
ROOT_URLCONF = "config.urls"

# Plantillas
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# Django REST Framework y autenticación JWT
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}

# Base de datos PostgreSQL
DATABASES = {
   "default": {
       "ENGINE": "django.db.backends.postgresql",
       "NAME": os.environ.get("DB_NAME"),
       "USER": os.environ.get("DB_USER"),
       "PASSWORD": os.environ.get("DB_PASSWORD"),
       "HOST": os.environ.get("DB_HOST", "localhost"),
       "PORT": os.environ.get("DB_PORT", "5432"),
  }
}

# Validación de contraseñas
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

# Idioma y zona horaria
LANGUAGE_CODE = "es-cl"
TIME_ZONE = "America/Santiago"
USE_I18N = True
USE_TZ = True

# Archivos estáticos
STATIC_URL = "static/"

# Correo de desarrollo: muestra los correos en la terminal
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Clave primaria predeterminada
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
