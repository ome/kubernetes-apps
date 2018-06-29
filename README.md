# kubernetes-apps

Kubernetes applications running in the OME.

See https://github.com/openmicroscopy/kubernetes-platform if you want to know more about the underlying infrastructure.


# List of deployed applications

## idr-redmine-tracker
The IDR submissions ticketing system https://idr-redmine.openmicroscopy.org/.
See https://idr.openmicroscopy.org/about/submission.html for more background on this project.


## jupyterhub-internal
An internal deployment of [JupyterHub](https://zero-to-jupyterhub.readthedocs.io/) for testing notebooks.


## jupyterhub-training
An internal deployment of [JupyterHub](https://zero-to-jupyterhub.readthedocs.io/) for testing training notebooks.
This will be removed when support for multiple notebook images is added to jupyterhub-internal.


## Monitoring
This comprises the following applications:
- grafana-global
- grafana-playground
- monitoring-oauth2
- prometheus-global
- prometheus-k8s
- prometheus-ome

See [docs/monitoring.md](docs/monitoring.md) for details.


# Documentation
- [Deploying applications](docs/deployment.md)
- [Developing applications](docs/development.md) (Work in progress)
