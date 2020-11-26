from flask import abort
from flask_restful import Resource, request
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required
from briochefood.models import User
from briochefood.ext.serialization import LoginSchema, UserSchema

from datetime import timedelta


class UserResource(Resource):
    @jwt_required
    def get(self):
        """Get all users"""
        users = User.query.all() or abort(204, "No items found")
        schema = UserSchema(many=True)
        return schema.jsonify(users)


class UserItemResource(Resource):
    @jwt_required
    def get(self, user_id):
        """Get user"""
        user = User.query.filter_by(
            id=user_id).first() or abort(404, "Item not found")
        schema = UserSchema(many=False)
        return schema.jsonify(user)


class UserLoginResource(Resource):
    def post(self):
        """User Login"""
        schema = LoginSchema()
        data = schema.load(request.get_json(force=True))

        user = User.query.filter_by(
            email=data['email'], password=data['password']).first() or abort(
                404, "Item not found"
        )

        access_token = create_access_token(
            identity=user.id, expires_delta=timedelta(seconds=60*60*24))
        refresh_token = create_refresh_token(identity=user.id)

        return {"access_token": access_token, "refresh_token": refresh_token}
