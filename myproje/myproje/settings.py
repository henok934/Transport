import os
from pathlib import Path

# 1. BASE DIRECTORY DEFINED FIRST
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. SECURITY SETTINGS (Production Grade)
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'your-default-secret-key')
# settings.py ውስጥ
DEBUG = False  # <-- ወደ False ይለውጡት
ALLOWED_HOSTS = [
    'fermataa-3ooq.onrender.com',
    'wedehagertransport.onrender.com',
    '.onrender.com',
    'localhost',
    '127.0.0.1'
]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# Security Headers
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True

# Strict Transport Security (HSTS) - 1 Year
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

REFERRER_POLICY = 'same-origin'

# Cookie Security
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True


# 3. APPLICATION DEFINITION
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third Party Apps
    'rest_framework',
    'drf_spectacular',
    'corsheaders',
    'axes',
    'csp',    
    # Your Apps
    'users',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'csp.middleware.CSPMiddleware', # <-- CSP Middleware በትክክል ተቀምጧል
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'axes.middleware.AxesMiddleware',
]



# Content Security Policy Settings (CSP)
# --- አዲሱ የ CSP 4.0+ ውቅር ---
# Content Security Policy Settings (CSP)
PERMISSIONS_POLICY = {
    "geolocation": [],
    "camera": [],
    "microphone": [],
}

CONTENT_SECURITY_POLICY = {
    'DIRECTIVES': {
        'default-src': ("'self'",),
        'img-src': ("'self'", 'data:', 'https:'),
        'script-src': ("'self'",),
        'style-src': ("'self'", "'unsafe-inline'", 'https://fonts.googleapis.com'),
    }
}

ROOT_URLCONF = 'myproje.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'users/templates')],
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

WSGI_APPLICATION = 'myproje.wsgi.application'

# 4. DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 5. AUTHENTICATION & USERS
AUTH_USER_MODEL = 'users.CustomUser'
AUTHENTICATION_BACKENDS = [
    'axes.backends.AxesStandaloneBackend',
    'django.contrib.auth.backends.ModelBackend',
]
AXES_ENABLED = False

# 6. EMAIL SETTINGS
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'teklemariammossie1@gmail.com'
EMAIL_HOST_PASSWORD = 'xbbdaymgoqapntds'
DEFAULT_FROM_EMAIL = 'teklemariammossie697@gmail.com'

# 7. STATIC & MEDIA FILES
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'users/static')]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 8. CORS & CSRF
CORS_ALLOW_ALL_ORIGINS = True

CSRF_TRUSTED_ORIGINS = [
    'https://wedehagertransport.onrender.com',
    'https://fermataa-3ooq.onrender.com',
]

# 9. INTERNATIONALIZATION
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Addis_Ababa'
USE_I18N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
}
