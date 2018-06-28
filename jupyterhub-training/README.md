# JupyterHub Training

Internal deployment of JupyterHub for training
Application URL: https://ome-lochy.openmicroscopy.org/jupyterhub-training/


## Installation

    helm repo add jupyterhub https://jupyterhub.github.io/helm-chart/
    helm repo update
    helm upgrade --install jupyter-train --namespace=jupyter-train \
        jupyterhub/jupyterhub --version=v0.7-d617e0a \
        -f zero-to-jupyterhub-config.yml -f path/to/zero-to-jupyterhub-secret.yml


## Post-installation

Check if JupyterHub is ready:

    kubectl --namespace=jupyter-train get pods

Follow JupyterHub logs:

    kubectl --namespace=jupyter-train logs -f deploy/hub
