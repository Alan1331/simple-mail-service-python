from flask_restful import Resource
from flask_jwt_extended import get_jwt, jwt_required

from app.datasource_example import blocklist

class LogoutResource(Resource):
    @jwt_required()  # Requires a valid JWT token
    def post(self):
        jti = get_jwt()['jti']
        blocklist.add(jti)  # Add the token JTI to the blacklist
        return {'message': 'User logged out successfully'}