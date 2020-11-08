# Описание

Репка с д\з и тестовыми проектами для учебного курса

---

## Python

### Flask

Фреймворк для разработки

[Мега-Учебник Flask, Часть 2: Шаблоны (издание 2018)](https://habr.com/ru/post/346340/)

Интерактивный терминал:

`flask shell`

Создание миграций по обновлённым моделям:

`flask db migrate -m "posts table"`

Накатывание миграций на бд:

`flask db upgrade`

### Gunicorn

Сервер приложений

[docs.gunicorn.org](https://docs.gunicorn.org/en/latest/index.html)

## Docker и Kubernetes

[docker хаб, начало работы](https://docs.docker.com/docker-hub/)

[странный пример сборки в докере](https://habr.com/ru/post/486202/)

[миникуб](https://minikube.sigs.k8s.io/docs/start/)

[дашборд](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/)

[маршрутизация](https://kubernetes.io/docs/concepts/services-networking/ingress/)

[тулза для анализа и оптимизации образов](https://github.com/wagoodman/dive)

[prometheus-stack](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack)

### Helm (2)

Как поставить и настроить

```bash
kubectl create serviceaccount tiller --namespace kube-system
kubectl create clusterrolebinding tiller-role-binding --clusterrole cluster-admin --serviceaccount=kube-system:tiller
helm init --service-account tiller
```

### Minikube

Внутри миникуба есть свой собственный докер и все образы нужно пушить именно туда, а не в локальный.

Можно перенастроить, чтобы он ходил за образами в сам хост, но зачем?)

### Полезные команды

[большая шпаргалка](https://kubernetes.io/ru/docs/reference/kubectl/cheatsheet/)

Смотреть за жизнью кластера в реальном времени:

`watch kubectl get all`
`watch kubectl get all -o wide`

Посмотреть список подов с метками:

`kubectl get po --show-labels`

Получить адрес сервиса по его имени:

`minikube service %name% --url -n %namespace%`

Терминал внутрь миникубика:

`minikube ssh`

## Skaffold

[Автоматизация сборки\деплоя в кубик](https://skaffold.dev/)
