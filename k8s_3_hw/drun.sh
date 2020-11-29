set -o allexport; source .env; set +o allexport
docker run --env-file .env -p 127.0.0.1:$FLASK_RUN_PORT:$FLASK_RUN_PORT/tcp --name=$APP_TAG ninib/$APP_TAG:latest | grep FLASK
docker rm $APP_TAG