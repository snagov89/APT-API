#!/usr/bin/env bash

echo "Running for ${ENVIRONMENT}."
if [ "${ENVIRONMENT}" = "prod" ] ; then
    poetry run gunicorn --config docker/gunicorn_config.py run:app --bind 0.0.0.0:${FLASK_RUN_PORT}
else
    poetry run python run.py
fi
