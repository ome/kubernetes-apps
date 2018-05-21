# JupyterHub Internal

Internal deployment of JupyterHub
Application URL: https://ome-lochy.openmicroscopy.org/jupyterhub-internal/


## Installation

    helm repo add jupyterhub https://jupyterhub.github.io/helm-chart/
    helm repo update
    helm upgrade --install jupyter-int --namespace=jupyter-int \
        jupyterhub/jupyterhub --version=v0.7-d617e0a \
        -f zero-to-jupyterhub-config.yml -f path/to/zero-to-jupyterhub-secret.yml


## Post-installation

Check if JupyterHub is ready:

    kubectl --namespace=jupyter-int get pods

Follow JupyterHub logs:

    kubectl --namespace=jupyter-int logs -f deploy/hub
