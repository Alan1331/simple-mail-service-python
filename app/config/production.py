from datetime import timedelta

class ProductionConfig:
    DEBUG = False
    JWT_SECRET_KEY = 'simplemailappbymr1331'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=30)