#!/bin/bash

docker exec ufapi bash -c "rm -f /uf_api/db.sqlite3"
docker exec ufapi bash -c "python /uf_api/manage.py migrate"
docker exec ufapi bash -c "nohup Xvnc :10 & python /uf_api/manage.py scrap"
