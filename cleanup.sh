kubectl config use-context minikube
kubectl delete ingress --all
kubectl delete all --all
docker container prune --force
docker rmi $(docker images --filter "dangling=true" -q --no-trunc)