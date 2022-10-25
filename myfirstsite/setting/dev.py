from myfirstsite.settings import *

SECRET_KEY = 'django-insecure-znc9ds3cy+5$4ow))bk_3p^1@o=sz0=+cvr)u24(2o7z))ych)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 2


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


STATIC_Root=BASE_DIR/'static'
MEDIA_Root=BASE_DIR/'media'


STATICFILES_DIRS = [
    BASE_DIR / "statics",
]

X_FRAME_OPTIONS = 'SAMEORIGIN' 