set -e

python manage.py makemigrations
python manage.py migrate --noinput
python manage.py collectstatic --noinput
gunicorn Gabrielle_Kourdadze.wsgi -b 0.0.0.0:8000 --workers=1 --timeout=300
#uvicorn Gabrielle_Kourdadze.asgi:application --host 0.0.0.0 --port 8000
