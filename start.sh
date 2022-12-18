#!/bin/bash

retry=10
echo -n "Trying migrations"
for i in $(seq $retry)
do
  echo -n .
  python manage.py migrate && break
  sleep 1
done

echo "=Starting runserver="
gunicorn wsgi:application \
         --bind 0.0.0.0:80\
