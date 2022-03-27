import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
import cloudinary

from petstagram.utils import is_production

BASE_DIR = Path(__file__).resolve().parent.parent


#This should be changed
'''
Dev -> Whatever
Proc -> Hidden and very strong
'''
SECRET_KEY = os.getenv('SECRET_KEY', '')

# SECURITY WARNING: don't run with debug turned on in production!
#This should be changed
'''
Dev -> True
Proc -> False
'''
DEBUG = os.getenv('DEBUG', 'False') == 'True'
APP_ENVIRONMENT = os.getenv('APP_ENVIRONMENT', 'Development')
'''
'False' == 'True' => False
'True' == 'True' => True
'''
#This should be changed
'''
Dev -> localhost , 127.0.0.1
Proc -> petstagram-project.herokuapp.com
'''
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(' ')


# Application definition
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = ()
WEB_APPS = (
    'petstagram.main',
    'petstagram.accounts',
)
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + WEB_APPS

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'petstagram.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'petstagram.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
#This should be changed
DATABASES = None
# DEFAULT_DATABASE_CONFIG = {
#     'ENGINE': 'django.db.backends.sqlite3',
#     'NAME': 'db.sqlite3',
# }

# if is_production():
DEFAULT_DATABASE_CONFIG = {
    'ENGINE': 'django.db.backends.postgresql',
    'HOST': os.getenv('DB_HOST', '127.0.0.1'),
    'PORT': os.getenv('DB_PORT', '5432'),  # if no env variable DB_PORT -> return 5432
    'NAME': os.getenv('DB_NAME', 'petstagram_db'),
    'USER': os.getenv('DB_USER', 'postgres'),
    'PASSWORD': os.getenv('DB_PASSWORD', 'mysecretpassword'),
}

DATABASES = {
    'default': DEFAULT_DATABASE_CONFIG,
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators
#This should be changed
AUTH_PASSWORD_VALIDATORS = []
if is_production():
    AUTH_PASSWORD_VALIDATORS.extend([
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
    ])


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR/ 'staticfiles')

STATICFILES_DIRS = (
   os.path.join(BASE_DIR / 'static'),
)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = 'media/'

MEDIA_ROOT = BASE_DIR / 'mediafiles'


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGGING_LEVEL = 'DEBUG'
if is_production():
    LOGGING_LEVEL = 'INFO'

LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            # DEBUG, WARNING , INFO, ERROR, CRITICAL
            'level': LOGGING_LEVEL,
            'filters': [],
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'INFO',
            'handlers': ['console'],
        }
    }
}

AUTH_USER_MODEL = 'accounts.PetstagramUser'
cloudinary.config(
  cloud_name = os.getenv('CLOUDINARY_CLOUD_NAME', None),
  api_key = os.getenv('CLOUDINARY_API_KEY', None),
  api_secret = os.getenv('CLOUDINARY_SECRET', None),
)