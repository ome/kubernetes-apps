# Jupyterhub Internal

Internal deployment of Jupyterhub
Application URL: https://ome-lochy.openmicroscopy.org/jupyterhub-internal/


## Installation

    helm repo add jupyterhub https://jupyterhub.github.io/helm-chart/
    helm repo update
    helm upgrade --install jupyter-int --namespace=jupyter-int \
        jupyterhub/jupyterhub --version=v0.6 \
        -f zero-to-jupyterhub-config.yml -f path/to/zero-to-jupyterhub-secret.yml


### Temporary installation instructions

Using Pull request https://github.com/jupyterhub/zero-to-jupyterhub-k8s/pull/649

    git clone https://github.com/jupyterhub/zero-to-jupyterhub-k8s.git
    cd zero-to-jupyterhub-k8s/
    git fetch origin pull/649/head
    git checkout FETCH_HEAD
    git describe
    # v0.6-261-g39dbd7a
    cd ..
    helm upgrade --install jupyter-int --namespace=jupyter-int \
        --wait --timeout 600 --force \
        ./zero-to-jupyterhub-k8s/jupyterhub/ \
        -f zero-to-jupyterhub-temporary.yml \
        -f zero-to-jupyterhub-config.yml -f path/to/zero-to-jupyterhub-secret.yml


## Post-installation

Check if jupyterhub is ready:

    kubectl --namespace=jupyter-int get pods

Follow JupyterHub logs:

    kubectl --namespace=jupyter-int logs -f deploy/hub
