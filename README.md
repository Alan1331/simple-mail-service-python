# simple-mail-service-python
Simple mail backend services built using Python with Flask libraries: Flask-RESTfull, flask-jwt-extended, and so on.
## System Architecture

This application or system adheres microservices-based architecture which means each feature is bundled in an independent service and not affect each other. Here is the following system diagram to learn more about the architecture:

![](https://github.com/Alan1331/simple-mail-service-python/blob/main/img/system-diagram.png?raw=true)
## Tech Stack
- Python
- Flask
- JWT
- Kubernetes
- Docker
- MongoDB
- Redis
## Project Structure

- [ ] `*service`: root directory of each service.
  - [ ] `app/`: contains application source-code.
    - [ ] `__init__.py`: initialization code.
    - [ ] `config/`: contains configuration settings for some environment.
    - [ ] `models/`: defines datasource layer.
    - [ ] `resources/`: defines all endpoints and their logic.
    - [ ] `utils/`: contains helper functions.
    - [ ] `routes.py`: defines route for all endpoints.
  
  - [ ] `docs/`: contains documentation for this service, ex: API docs.
  - [ ] `run.py`: file to run the service. It will trigger the initialization code when it's running.
  - [ ] `requirements.txt`: defines all dependencies of the service.
  - [ ] `Dockerfile`: file to build docker image of the service.

- [ ] `img/`: contains all images.
- [ ] `k8s/`: contains all kubernetes deployment files.

## Deployment

You need a kubernetes cluster to deploy this project. Here are the following steps for the deployment:
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
## API Documentations

Here are the following API documentations for each service:
- [core-api-service](https://github.com/Alan1331/simple-mail-service-python/blob/main/core-api-service/docs/api.md)
- [user-api-service](https://github.com/Alan1331/simple-mail-service-python/blob/main/user-service/docs/api.md)
- [mail-api-service](https://github.com/Alan1331/simple-mail-service-python/blob/main/mail-service/docs/api.md)
## Author

- [Syekh Maulana "Alan" Wijaya](https://github.com/Alan1331)