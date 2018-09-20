# JupyterHub ITR

Internal deployment of JupyterHub for testing the ITR
Application URL: https://ome-lochy.openmicroscopy.org/jupyterhub-itr/


## Installation

See [helmfile.yaml](../helmfile.yaml)

Note: When upgrading from a previously installed version you may sometimes need to add the flag `--force` due to changes in labels.


## Post-installation

Check if JupyterHub is ready:

    kubectl --namespace=jupyter-itr get pods

Follow JupyterHub logs:

    kubectl --namespace=jupyter-itr logs -f deploy/hub
