#!/bin/bash

function print_error {
    echo "$1" >&2
    exit 1
}

virtualenv virtualenv || print_error "Couldn't make virtualenv"

./virtualenv/bin/pip install -r requirements.txt || print_error "couldn't install requirement.txt packages"

./virtualenv/bin/python src/uf_api/manage.py runserver 0.0.0.0:8080
