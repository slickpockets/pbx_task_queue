Celery task queue for pushing sms messages from truexpro to pbx server by way of python celery.

to begin a single worker to begin executing tasks:


celery -A celery_worker.celery worker --loglevel=info --pool=solo

in alt terminal run python run.py

expects a .env file with the following terms:
TESTING=
DEBUG=
FLASK_ENV=
SECRET_KEY=
