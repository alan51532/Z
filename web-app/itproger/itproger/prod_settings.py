

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '80s3nаgcе593qkчl#юbс(y1mbs-эяl6#70vsnqc0il5je!s!d)'

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']

STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"


