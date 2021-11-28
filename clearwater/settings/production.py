from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv("DB_NAME"),
        'USER': os.getenv("DB_USER"),
        'PASSWORD': os.getenv("DB_PASS"),
        'HOST': os.getenv("DB_HOST"),
    }
}

SECRET_KEY = os.getenv("SECRET_KEY")

ALLOWED_HOSTS = [os.getenv("ALLOWED_HOSTS")] 

try:
    from .local import *
except ImportError:
    pass
