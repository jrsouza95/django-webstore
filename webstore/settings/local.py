from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INSTALLED_APPS += ('debug_toolbar', 'rest_framework', 'django_filters')