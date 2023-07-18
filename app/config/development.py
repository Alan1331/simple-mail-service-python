from datetime import timedelta

class DevelopmentConfig:
    DEBUG = True
    JWT_SECRET_KEY = 'simplemailappbymr1331'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=10)