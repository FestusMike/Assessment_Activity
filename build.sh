#!/usr/bin/env bash

set -o errexit

pip install -r requirements.txt
python manage.py makemigrations users
python manage.py migrate
python manage.py collectstatic --no-input
