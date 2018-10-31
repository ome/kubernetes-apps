# Generic webapp

A generic helm chart for deploying self-contained single-container single-pod stateless web services.

See [`values.yaml`](values.yaml) for all parameters.

For a typical web-app the following may need to be configured:
- `image.repository`: Docker image for the web-app (required)
- `image.tag`: Image tag, default `latest` but you should use a released tag in production
- `internalPort`: Internal container port that the web-app is running on, default `80`
