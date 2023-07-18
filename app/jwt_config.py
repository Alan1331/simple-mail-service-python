from flask_jwt_extended import JWTManager
from app.datasource_example import blocklist

jwt = JWTManager()

@jwt.token_in_blocklist_loader
def check_if_token_in_blocklist(jwt_header, jwt_payload: dict):
    jti = jwt_payload['jti']
    token_in_blocklist = jti in blocklist
    return token_in_blocklist