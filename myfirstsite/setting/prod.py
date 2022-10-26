from myfirstsite.settings import *
from django.core import mail


SECRET_KEY = 'django-insecure-znc9ds3cy+5$4ow))bk_3p^1@o=sz0=+cvr)u24(2o7z))ych)'

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = False
DEBUG = True

ALLOWED_HOSTS = ['*']

SITE_ID = 2

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


STATIC_Root=BASE_DIR/'static'
MEDIA_Root=BASE_DIR/'media'
STATIC_DEPS=True

COMPRESS_ROOT= STATIC_Root
STATICFILES_DIRS = [
    BASE_DIR / "statics",
]
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)
CSRF_COOKIE_SECURE=True
AUTHENTICATION_BACKENDS = ['accounts.backends.EmailBackend'] 

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'mohi.fk9@gmail.com'
EMAIL_HOST_PASSWORD = 'lidszzzoyxcpsxso' #past the key or password app here
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'default from email'
DEFAULT_EMAIL_FROM = 'mohi.fk9@gmail.com' 