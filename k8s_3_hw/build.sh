set -o allexport; source .env; set +o allexport
docker build ./flask_app -t "ninib/$APP_TAG"