kubectl delete crd prometheuses.monitoring.coreos.com
kubectl delete crd prometheusrules.monitoring.coreos.com
kubectl delete crd servicemonitors.monitoring.coreos.com
kubectl delete crd podmonitors.monitoring.coreos.com
kubectl delete crd alertmanagers.monitoring.coreos.com
kubectl delete crd thanosrulers.monitoring.coreos.com
kubectl delete crd probes.monitoring.coreos.com

helm delete monitoring --purge

helm install --name=monitoring --namespace=monitoring prometheus-community/kube-prometheus-stack --version=9.3.4