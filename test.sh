#!/bin/bash
source ./private_vars.sh

python manage.py collectstatic --noinput
python manage.py compress
python manage.py collectstatic --noinput
coverage manage.py test
coveralls