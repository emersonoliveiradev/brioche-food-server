from flask import abort
from flask_restful import Resource
from briochefood.models import User
from briochefood.ext.serialization import UserSchema


class UserResource(Resource):
    def get(self):
        """Get all users"""
        users = User.query.all() or abort(204, "No items found")
        schema = UserSchema(many=True)
        return schema.jsonify(users)


class UserItemResource(Resource):
    def get(self, user_id):
        """Get user"""
        user = User.query.filter_by(
            id=user_id).first() or abort(404, "Item not found")
        schema = UserSchema(many=False)
        return schema.jsonify(user)
