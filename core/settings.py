import os
from datetime import timedelta
from .secrets import SECRET_KEY, BASE_DIR, DATABASES

ALLOWED_HOSTS = []
DEBUG = True

ROOT_URLCONF = "core.urls"

INSTALLED_APPS = [

 "django.contrib.admin",
 "django.contrib.contenttypes",
 "django.contrib.staticfiles",
 "django.contrib.auth",
 "django.contrib.sessions",
 "django.contrib.humanize",
 "django.contrib.messages",
 "sass_processor",
 "corsheaders",
 "core",
]


TEMPLATES = [{
 "BACKEND": "django.template.backends.django.DjangoTemplates",
 "APP_DIRS": True,
 "OPTIONS": {
  "context_processors": [
   "django.template.context_processors.request",
   "django.contrib.auth.context_processors.auth",
   "django.contrib.messages.context_processors.messages"
  ],
 },
}]

MIDDLEWARE = [
 "django.contrib.sessions.middleware.SessionMiddleware",
 "django.middleware.common.CommonMiddleware",
 "django.middleware.csrf.CsrfViewMiddleware",
 "django.contrib.auth.middleware.AuthenticationMiddleware",
 "htmlmin.middleware.HtmlMinifyMiddleware",
 "htmlmin.middleware.MarkRequestMiddleware",
 "corsheaders.middleware.CorsMiddleware",
 "django.middleware.security.SecurityMiddleware",
 'django.contrib.messages.middleware.MessageMiddleware',
 'django.middleware.clickjacking.XFrameOptionsMiddleware',

]


LOGIN_URL = "/login/"

STATIC_URL = "/static/"
if DEBUG:
    MEDIA_ROOT = os.path.join(BASE_DIR, "uploads")
    STATIC_ROOT = os.path.abspath(f"{BASE_DIR}/static")
else:
     MEDIA_ROOT = os.path.join(BASE_DIR, "..", "uploads")
     STATIC_ROOT = os.path.abspath(f"{BASE_DIR}/../static")
MEDIA_URL = "/uploads/"
SASS_PROCESSOR_ROOT = os.path.abspath(os.path.join(BASE_DIR, "core", "static"))

CORS_ORIGIN_ALLOW_ALL = True

USE_TZ = True
TIME_ZONE = "Europe/London"