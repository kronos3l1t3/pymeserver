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

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)
