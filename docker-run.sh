#!/bin/bash

docker run -d -p 8080:8080 -p 5910:5910 -e "DISPLAY=:10" --name ufapi --rm ufapi
