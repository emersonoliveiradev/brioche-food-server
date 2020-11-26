from flask import abort
from flask_restful import Resource, request
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required
from briochefood.models import Address, User
from briochefood.ext.database import db
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


class UserRegisterResource(Resource):
    def post(self):
        """User register"""
        try:
            schema = UserSchema()
            data = schema.load(request.get_json(force=True))

            address = Address(
                street=data['address'].get("street", None),
                number=data['address'].get("number", None),
                complement=data['address'].get("complement", None),
                district=data['address'].get("district", None),
                city=data['address'].get("city", None),
                zipcode=data['address']['zipcode'],
                state=data['address']['state'],
                country=data['address']['country'],
            )
            db.session.add(address)
            db.session.flush()

            user = User(name=data['name'],
                        lastname=data['lastname'],
                        email=data['email'],
                        password=data['password'],
                        cpf=data['cpf'],
                        birth_date=data['birth_date'],
                        phone=data['phone'])
            db.session.add(user)
            db.session.flush()

            db.session.commit()
            return schema.jsonify(user)
        except Exception as e:
            db.session.rollback()
            abort(400, "Registration not performed. " + str(e))
        return "ok"
