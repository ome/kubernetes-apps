# JupyterHub Internal

Internal deployment of JupyterHub
Application URL: https://ome-lochy.openmicroscopy.org/jupyterhub-internal/


## Installation

    helm repo add jupyterhub https://jupyterhub.github.io/helm-chart/
    helm repo update
    helm upgrade --install jupyter-int --namespace=jupyter-int \
        jupyterhub/jupyterhub --version=v0.7-e2757f0 \
        -f zero-to-jupyterhub-config.yml -f path/to/zero-to-jupyterhub-secret.yml

Note: When upgrading from the previously installed version `v0.7-d617e0a` you must add the flag `--force` due to changes in labels.


## Post-installation

Check if JupyterHub is ready:

    kubectl --namespace=jupyter-int get pods

Follow JupyterHub logs:

    kubectl --namespace=jupyter-int logs -f deploy/hub
