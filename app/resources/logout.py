from flask_restful import Resource
from flask_jwt_extended import get_jwt, jwt_required

from app.models.jwt_blocklist import JwtBlocklist

class LogoutResource(Resource):
    @jwt_required()  # Requires a valid JWT token
    def post(self):
        jti = get_jwt()['jti']
        # Add the token JTI to the blocklist
        token_object = {
            'token': jti
        }
        JwtBlocklist.add_token(token_object)

        return {'message': 'User logged out successfully'}