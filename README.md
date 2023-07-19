# simple-mail-service-python
Simple mail backend service built using Python with Flask libraries: Flask-RESTfull, flask-jwt-extended, and so on.

## Deployment

To deploy this project on local server, run the following command to install all dependencies:

```bash
pip install -r requirements.txt
```

Create '.env' file by copying '.env.example' file on project root directory:

```bash
cp .env.example .env
```

Modify the '.env' file content to match your environment settings. After that, execute 'run.py' to run the mail service:

```bash
python3 run.py
```