#!/bin/bash
source ./private_vars.sh

python3 ./manage.py collectstatic --noinput
python3 ./manage.py compress
python3 ./manage.py collectstatic --noinput
python3 ./manage.py runserver


