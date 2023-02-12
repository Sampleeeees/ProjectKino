#!/bin/sh

if [ "$DATABASE" = "postgres"]
then
  echo "Waiting for postgres..."

  while ! nc port $DB_HOST $DB_PORT; do
    sleep 0.1
  done

fi

python manage.py flush --no-input
python manage.py migrate

exec "$@"