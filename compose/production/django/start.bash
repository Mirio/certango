#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

export DATABASE_URL="postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}/${POSTGRES_DB}"
env

cd "${HOME}"
source "${HOME}/.venv/bin/activate"

python manage.py collectstatic --noinput

if [[ ${COMPRESS_ENABLED} == "true" ]]; then
  python /app/manage.py compress
fi

echo "Waiting for PostgreSQL to become available..."
while ! nc -z "${POSTGRES_HOST}" ${POSTGRES_PORT}; do
  sleep 1
done
echo 'PostgreSQL is available.'

python manage.py migrate
gunicorn config.wsgi --bind 0.0.0.0:8000 --chdir=.
