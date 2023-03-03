#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

export DATABASE_URL="postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}/${POSTGRES_DB}"

cd "${HOME}"
source "${HOME}/.venv/bin/activate"

python manage.py migrate
python manage.py runserver_plus 0.0.0.0:8000
