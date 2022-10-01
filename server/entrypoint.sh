#!/bin/sh
# wait-for-postgres.sh

set -e
  
host="db:5432"

until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$host" -U "postgres" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done
  
>&2 echo "Postgres is up - executing command"

poetry run python manage.py migrate
poetry run python manage.py createsuperuser --noinput --username admin --email admin@admin.com

exec "$@"
