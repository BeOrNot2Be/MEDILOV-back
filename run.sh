#!/bin/bash
./private_vars.sh

export SMTP_SERVER=mail.privateemail.com
export SMTP_USER=someone@mail.com
export SMTP_PASSWORD=smpassword

python manage.py collectstatic --noinput
python manage.py compress
python manage.py collectstatic --noinput
python manage.py runserver