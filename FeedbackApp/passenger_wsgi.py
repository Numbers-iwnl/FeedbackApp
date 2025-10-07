# passenger_wsgi.py — Hostinger entry point for a Django app
import os
import sys
from pathlib import Path

# Ensure the project root is on the Python path
BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

# Point to your Django settings module (package name must match your project)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FeedbackApp.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
