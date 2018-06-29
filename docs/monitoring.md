# Monitoring

Deploys Prometheus and Grafana to monitor internal OMERO servers and the IDR.

## Components

- grafana-global https://monitoring.openmicroscopy.org/grafana-global: Curated dashboards.
- grafana-playground https://monitoring.openmicroscopy.org/grafana-playground: Grafana server for anyone to try out dashboards, configuration, etc. May be wiped without warning.
- monitoring-oauth2 https://monitoring.openmicroscopy.org/prometheus-oauth2: GitHub OAuth for all prometheus-global, prometheus-k8s, prometheus-ome. Do not access directly, you should be redirected automatically.
- prometheus-global https://monitoring.openmicroscopy.org/prometheus-global: Prometheus server for gathering federated metrics from internal and external prometheus servers for long-term storage.
- prometheus-k8s https://monitoring.openmicroscopy.org/prometheus-k8s: Prometheus server for internal Kubernetes self-monitoring.
- prometheus-ome https://monitoring.openmicroscopy.org/prometheus-ome: Prometheus server for internal OMERO servers.

## Deployment

This can be deployed in two ways.

### Shell script
The python script `helmfile-sync.py` is a partial reimplementation of helmfile that prints out shell commands:
```
python helmfile-sync.py --dry-run
```
```
helm upgrade --install nginx-ingress stable/nginx-ingress --version 0.20.3 --namespace nginx-ingress --values nginx-ingress/nginx-ingress.yml
helm upgrade --install grafana-playground-storage ./charts/nfs-volume --namespace monitoring --values grafana-playground/nfs-volume.yml
helm upgrade --install grafana-playground stable/grafana --version 1.10.2 --namespace monitoring --values grafana-playground/grafana.yml --values ../config/grafana-playground/grafana-secret.yml
helm upgrade --install grafana-global-storage ./charts/nfs-volume --namespace monitoring --values grafana-global/nfs-volume.yml
helm upgrade --install grafana-global stable/grafana --version 1.10.2 --namespace monitoring --values grafana-global/grafana.yml --values ../config/grafana-global/grafana-secret.yml
helm upgrade --install monitoring-oauth2 ./charts/oauth2-proxy --namespace monitoring --values monitoring-oauth2/oauth2-proxy.yml --values ../config/monitoring-oauth2/oauth2-proxy.yml
helm upgrade --install prometheus-k8s-storage ./charts/nfs-volume --namespace monitoring --values prometheus-k8s/nfs-volume.yml
helm upgrade --install prometheus-k8s stable/prometheus --version 6.7.4 --namespace monitoring --values prometheus-k8s/prometheus.yml
helm upgrade --install prometheus-ome-storage ./charts/nfs-volume --namespace monitoring --values prometheus-ome/nfs-volume.yml
helm upgrade --install prometheus-ome stable/prometheus --version 6.7.4 --namespace monitoring --values prometheus-ome/prometheus.yml --values ../config/prometheus-ome/prometheus.yml
helm upgrade --install prometheus-global-storage ./charts/nfs-volume --namespace monitoring --values prometheus-global/nfs-volume.yml
helm upgrade --install prometheus-global stable/prometheus --version 6.7.4 --namespace monitoring --values prometheus-global/prometheus.yml --values ../config/prometheus-global/prometheus.yml
```
Redirect this into a shell script and run it. Alternatively drop the `--dry-run` argument.

### Helmfile
Install helmfile and run
```
helmfile sync
```
You can also do a partial deployment by passing a `key: value` pair from the `labels` section of `helmfile.yaml`, e.g.
```
helmfile --selector app=grafana sync
```
