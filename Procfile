release: python manage.py migrate
web: gunicorn pymeserver.asgi:application --log-file - -k uvicorn.workers.UvicornWorker
