# Nginx Ingress

Nginx default Kubernetes Ingress.


## Pre-installation

Create HTTPS certificate secret:
```
kubectl create --namespace=kube-system secret tls star-openmicroscopy-org-<date> --key PRIVATE.key --cert CERTIFICATE.crt+bundle
```

Ensure `default-ssl-certificate` in [`nginx-ingress.yml`](nginx-ingress.yml) corresponds to `star-openmicroscopy-org-<date>`.

When changing a certificate you may need to force a restart of the nginx-ingress pods:

```
kubectl -n nginx-ingress delete pods -l app=nginx-ingress,component=
controller
```
