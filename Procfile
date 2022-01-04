release: python manage.py migrate
web: gunicorn config.asgi:application --log-file - -k uvicorn.workers.UvicornWorker
