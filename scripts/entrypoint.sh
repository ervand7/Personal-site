#! /bin/bash

# shellcheck disable=SC2164
cd personal_site
python3.9 manage.py makemigrations
python3.9 manage.py migrate

python3.9 manage.py collectstatic --no-input
python3.9 manage.py loaddata db_dump.json
gunicorn personal_site.wsgi:application --bind 0.0.0.0:8000
