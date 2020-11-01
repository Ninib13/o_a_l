eval $(minikube docker-env)
set -o allexport; source .env; set +o allexport
docker build . -t "ninib/$APP_TAG"