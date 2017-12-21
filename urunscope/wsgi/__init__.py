import os
from django.core.wsgi import get_wsgi_application
from .health_check import health_check

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'urunscope.settings')
application = get_wsgi_application()
application = health_check(application, '/health/')
