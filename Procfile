release: python manage.py migrate
web: gunicorn config.asgi:application --log-file - -k uvicorn.workers.UvicornWorker
worker: celery worker --app=config.celery --loglevel=info -B
beat: celery beat --app=config.celery --loglevel=info