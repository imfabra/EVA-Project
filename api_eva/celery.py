from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Establece la configuración de Django para Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_eva.settings')

# Crea una instancia de la aplicación Celery
app = Celery('api_eva')

# Carga la configuración de la aplicación desde el archivo de configuración de Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Busca y registra automáticamente las tareas en tus aplicaciones Django
app.autodiscover_tasks()
