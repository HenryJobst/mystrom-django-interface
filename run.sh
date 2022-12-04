#!/bin/sh
docker run \
   --name mystrom-interface \
   -p 8000:8000 \
   -e DB_NAME=mystrom \
   -e DB_USER=mystrom \
   -e DB_PASSWORD=mystrom \
   -e DB_HOST=127.0.0.1 \
   -e DB_PORT=3336 \
   -e SECRET_KEY=myHiddenSecretKey \
   -e ALLOWED_HOSTS=localhost \
   -e CORS_ORIGIN_ALLOW_ALL=False \
   -e CORS_ORIGIN_WHITELIST=http://localhost:8000 \
   -e TZ=Europe/Berlin \
   nksdaoxxso/mystrom-django-interface
   