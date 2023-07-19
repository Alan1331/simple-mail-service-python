from flask_jwt_extended import JWTManager
from app.models.jwt_blocklist import JwtBlocklist

jwt = JWTManager()

@jwt.token_in_blocklist_loader
def check_if_token_in_blocklist(jwt_header, jwt_payload: dict):
    # Get jwt token from jwt payload
    jti = jwt_payload['jti']
    
    # Check if the token in blocklist collection
    blocklist = JwtBlocklist.get_token(jti)
    token_in_blocklist = blocklist != None

    return token_in_blocklist