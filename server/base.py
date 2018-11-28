"""
Django settings for server project.

Generated by 'django-admin startproject' using Django 1.9.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Login redirect
LOGIN_REDIRECT_URL = 'index'

# Application definition

INSTALLED_APPS = [
    'smartshark.apps.ServersharkConfig',
    'suit',
    'django_filters',
    'bootstrap3',
    'progressbarupload',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

FILE_UPLOAD_HANDLERS = (
    "progressbarupload.uploadhandler.ProgressBarUploadHandler",
    "django.core.files.uploadhandler.MemoryFileUploadHandler",
    "django.core.files.uploadhandler.TemporaryFileUploadHandler",
)

ROOT_URLCONF = 'server.urls'

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
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'server.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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

SERVERSHARK_VERSION = '0.1.3'
SUIT_CONFIG = {
    'ADMIN_NAME': 'ServerSHARK ' + SERVERSHARK_VERSION,
}

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

SUBSTITUTIONS = {
    'db_user': {'name': '$db_user', 'description': 'database username'},
    'db_password': {'name': '$db_password', 'description': 'database password'},
    'db_database': {'name': '$db_database', 'description': 'database name'},
    'db_hostname': {'name': '$db_hostname', 'description': 'hostname on which the database runs on'},
    'db_port': {'name': '$db_port', 'description': 'port on which the database listens'},
    'db_authentication': {'name': '$db_authentication', 'description': 'database used for authentication'},
    'path': {'name': '$path', 'description': 'path to the repository / the revision'},
    'plugin_path': {'name': '$plugin_path', 'description': 'path to the plugins root folder'},
    'project_name': {'name': '$project_name', 'description': 'Name of the project'},
    'revision': {'name': '$revision', 'description': 'revision hash of the revision which is processed'},
    'queue': {'name': '$queue', 'description': 'default job queue'},
    'cores_per_job': {'name': '$cores_per_job', 'description': 'cores per job (HPC only)'},
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'simple': {
            'format': '[%(asctime)s] %(levelname)s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file_debug': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': os.path.normpath(BASE_DIR + '/logs/debug.log'),
            'maxBytes': 1024 * 1024 * 8,
            'backupCount': 3
        },
        'file_info': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': os.path.normpath(BASE_DIR + '/logs/info.log'),
            'maxBytes': 1024 * 1024 * 8,
            'backupCount': 3
        },
        'file_error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': os.path.normpath(BASE_DIR + '/logs/error.log'),
            'maxBytes': 1024 * 1024 * 8,
            'backupCount': 3
        }
    },
    'loggers': {
        'hpcconnector': {
            'handlers': ['console', 'file_debug', 'file_info', 'file_error'],
            'level': 'DEBUG',
        },
        'django': {
            'handlers': ['console', 'file_debug', 'file_info', 'file_error'],
        },
        'py.warnings': {
            'handlers': ['console', 'file_debug', 'file_info', 'file_error'],
        },
        'root': {
            'handlers': ['file_debug', 'file_info', 'file_error'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}
