import dj_database_url
import os
from src.settings.local import *

DEBUG = False

GDAL_LIBRARY_PATH = os.environ.get('GDAL_LIBRARY_PATH')
GEOS_LIBRARY_PATH = os.environ.get('GEOS_LIBRARY_PATH')

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'Nomad',
        'USER':'postgres',
        'PASSWORD':'letmein20116199623',
        'HOST':'localhost',
        'PORT':5432
    }
}
CORS_ALLOWED_ORIGINS = [

]
# SSL and TLS settings
# CORS_REPLACE_HTTPS_REFERER = True
# HOST_SCHEME = "https://"
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_SECONDS = 1000000
# SECURE_FRAME_DENY = True

db_from_env = dj_database_url.config()
DATABASES["default"].update(db_from_env)
DATABASES["default"]["CONN_MAX_AGE"] = 500
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'


EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'test@mail.com')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', 'test')
EMAIL_PORT = 587
