# Jupyterhub Internal

Internal deployment of Jupyterhub
Application URL: https://ome-lochy.openmicroscopy.org/jupyterhub-internal/

## Installation

    helm repo add jupyterhub https://jupyterhub.github.io/helm-chart/
    helm repo update
    helm upgrade --install jupyter-int --namespace=jupyter-int \
        jupyterhub/jupyterhub --version=v0.6 \
        -f zero-to-jupyterhub-config.yml -f path/to/zero-to-jupyterhub-secret.yml

Check if jupyterhub is ready:

    kubectl --namespace=jupyter-int get pods

Follow JupyterHub logs:

    kubectl --namespace=jupyter-int logs -f deploy/hub
