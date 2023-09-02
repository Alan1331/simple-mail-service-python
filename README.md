# simple-mail-service-python
Simple mail backend services built using Python with Flask libraries: Flask-RESTfull, flask-jwt-extended, and so on.
## Deployment

You need a kubernetes cluster to deploy this project. Here is the following steps for deployment:
- Prepare a kubernetes cluster.
- Get into the cluster control plane to run kubectl commands.
- Clone this project repository and change your current working directory into the root of this project.
- Run the following commands to apply all deployment files:
```bash
kubectl apply -f k8s/*.yaml
```
- If the preceding command didn't work, try to apply each deployment file in /k8s directory one-by-one. For example:
```bash
kubectl apply -f k8s/core-api.yaml
```