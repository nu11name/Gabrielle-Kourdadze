set -e

python manage.py makemigrations
python manage.py migrate --noinput
python manage.py collectstatic --noinput
uvicorn Gabrielle_Kourdadze.asgi:application --host 0.0.0.0 --port 8000
