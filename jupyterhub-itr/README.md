# JupyterHub ITR

Internal deployment of JupyterHub for testing the ITR
Application URL: https://ome-lochy.openmicroscopy.org/jupyterhub-itr/


## Installation

    helm repo add jupyterhub https://jupyterhub.github.io/helm-chart/
    helm repo update
    helm upgrade --install jupyter-int --namespace=jupyter-int \
        jupyterhub/jupyterhub --version=v0.7-d4d1fb7 \
        -f zero-to-jupyterhub-config.yml -f path/to/zero-to-jupyterhub-secret.yml

Note: When upgrading from a previously installed version you may sometimes need to add the flag `--force` due to changes in labels.


## Post-installation

Check if JupyterHub is ready:

    kubectl --namespace=jupyter-itr get pods

Follow JupyterHub logs:

    kubectl --namespace=jupyter-itr logs -f deploy/hub
