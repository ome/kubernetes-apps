# JupyterHub Training

Internal deployment of JupyterHub for training
Application URL: https://ome-lochy.openmicroscopy.org/jupyterhub-training/


## Installation

See [helmfile.yaml](../helmfile.yaml)

Note: When upgrading from a previously installed version you may sometimes need to add the flag `--force` due to changes in labels.


## Post-installation

Check if JupyterHub is ready:

    kubectl --namespace=jupyter-train get pods

Follow JupyterHub logs:

    kubectl --namespace=jupyter-train logs -f deploy/hub
