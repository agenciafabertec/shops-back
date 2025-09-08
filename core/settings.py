import os, dj_database_url

DEBUG = os.environ.get("DJANGO_DEBUG","0") == "1"

ALLOWED_HOSTS = [
    os.environ.get("RENDER_EXTERNAL_HOSTNAME",""),  # ex: shops-backend.onrender.com
]

CSRF_TRUSTED_ORIGINS = [
    "https://" + os.environ.get("RENDER_EXTERNAL_HOSTNAME",""),
]

# Se o front ficar em domínio diferente (Vercel), libere CORS:
CORS_ALLOWED_ORIGINS = [
    "https://shops-mu.vercel.app",
]
