set -o allexport; source .env; set +o allexport
docker run -p 127.0.0.1:$FLASK_RUN_PORT:$FLASK_RUN_PORT/tcp --name=$APP_TAG ninib/$APP_TAG:latest
docker rm $APP_TAG