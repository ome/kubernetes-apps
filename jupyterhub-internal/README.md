# JupyterHub Internal

Internal deployment of JupyterHub
Application URL: https://ome-lochy.openmicroscopy.org/jupyterhub-internal/


## Installation

See [helmfile.yaml](../helmfile.yaml)

Note: When upgrading from a previously installed version you may sometimes need to add the flag `--force` due to changes in labels.


## Post-installation

Check if JupyterHub is ready:

    kubectl --namespace=jupyter-int get pods

Follow JupyterHub logs:

    kubectl --namespace=jupyter-int logs -f deploy/hub
