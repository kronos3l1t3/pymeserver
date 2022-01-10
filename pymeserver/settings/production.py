from .base import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ALLOWED_HOSTS = env("ALLOWED_HOSTS", default=["*"])
DEBUG = env("DEBUG", default=False)

DEFAULT_FILE_STORAGE = env.str("DJANGO_DEFAULT_FILE_STORAGE", default="django.core.files.storage.FileSystemStorage")

if "dropbox" in DEFAULT_FILE_STORAGE.lower():
    DROPBOX_OAUTH2_TOKEN = env.str("DROPBOX_OAUTH2_TOKEN", default="")
    DROPBOX_ROOT_PATH = env.str("DROPBOX_ROOT_PATH", default="/")

DATABASES = {
    'default': {
        'ENGINE': env.str("DJANGO_DB_ENGINE", default='django.db.backends.sqlite3'),
        'NAME': env.str("DJANGO_DB_NAME", default='db.sqlite3'),
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env.str("DJANGO_DB_NAME", default='dcum544ehm72kk'),
        'USER': env.str("DJANGO_USER_NAME", default='nwoujvfyzpmmxq'),
        'PASSWORD': env.str("DJANGO_USER_NAME", default='574d1db47c089b7f9dd5125853b31ad8ed152c6f9696472fee0bba8508eff9dc'),
        'HOST': env.str("DJANGO_DB_HOST", default='ec2-107-21-146-133.compute-1.amazonaws.com'),
        'PORT': env.str("DJANGO_DB_PORT", default='5432'),
    }
}

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)
