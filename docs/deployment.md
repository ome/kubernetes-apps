# Installing applications on the OME Kubernetes cluster

Applications and resource on Kubernetes can be managed in two ways:
- Individual resources/objects can be managed through Kubernetes manifests. An application will consist of several objects.
- An application may be packaged up into something called a "Helm chart".

This document contains some examples.
Consult the README.md for each app in this repository to find out how each application should be installed or configured.


## Prerequisites

Install the clients necessary to work with the Kubernetes cluster.
The versions of these clients are important and must be compatible with the server!

If you see version errors when connecting to the cluster, or if these instructions are out of date, please ask for help.

### kubectl
Install kubectl 1.9.x: https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-kubectl-binary-via-curl

If you are using homebrew the current version may be suitable (last checked 2018-03-01):

    brew install kubernetes-cli

### helm
Install helm 2.7.x: https://github.com/kubernetes/helm/releases

WARNING: Do not use homebrew, and do not install the latest version.

Setup your client-side configuration by running:

    helm init --client-only


## Access credentials

At present you must authenticate with the Kubernetes cluster using a private kubeconfig file containing a shared client certificate.
Fetch this file and either:
- Copy it to `~/.kube/config`; this will then be used by default
- Export the environment variable `KUBECONFIG=path/to/kubeconfig`

WARNING: This certificate currently enables full admin access.

Run:

    kubectl get nodes

If you have set everything up correctly you should see a list of nodes in the cluster, e.g.:

    NAME            STATUS    ROLES     AGE       VERSION
    ome-lochy-m01   Ready     master    17d       v1.9.2+coreos.0
    ome-lochy-n01   Ready     node      17d       v1.9.2+coreos.0
    ome-lochy-n02   Ready     node      17d       v1.9.2+coreos.0

Run:

    helm list

Check there are no errors.
If any applications have already been installed with helm they may be listed, e.g.

    NAME            REVISION        UPDATED                         STATUS         CHART                    NAMESPACE
    nginx-ingress   1               Tue Feb 20 15:15:27 2018        DEPLOYED       nginx-ingress-0.9.3      kube-system


## Installing applications from manifests

Simply run `kubectl apply -f`, passing either a manifest file or a directory of manifests, e.g.:

    kubectl apply -f idr-redmine-tracker/k8s/

`kubectl apply` should be idempotent and can be safely run multiple times.

The application may require additional secret manifests containing private configuration data.
These may be stored in other repositories.


## Installing applications with helm

Helm charts need to be downloaded before they can be deployed.
There are a set of charts that are configured by default.
Other chart repositories can be added using

    helm repo add https://EXAMPLE.ORG/chart/repo
    helm repo update

These repositories may be regularly updated, use `helm repo update` to update the list.

Most charts will require configuration which can be passed as command line arguments, or in the form of one or more configuration files.

For example, to install a chart run:

    helm upgrade --install NAME CHART/NAME -f path/to/config.yaml  -f path/to/secret.yaml

- `NAME` is your own name for the deployment, and on a shared cluster should be meaningful to others
- `CHART/NAME` is the name of the helm chart you are installing

If you are running multiple versions of the same application and it requires access to the Kubernetes API (for instance, to manage additional pods) you should either:
- Configure it so multiple versions won't conflict
- Put it in a separate namespace (e.g. `--namespace=NAME`)
