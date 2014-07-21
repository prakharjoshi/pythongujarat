#!/bin/bash
python manage.py runserver $OPENSHIFT_PYTHON_IP:$OPENSHIFT_PYTHON_PORT &
