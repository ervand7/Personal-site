#! /bin/bash

# shellcheck disable=SC2164
cd personal_site
celery -A subscribe beat --loglevel=DEBUG
