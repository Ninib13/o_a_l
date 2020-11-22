# -*- coding: utf-8 -*- 
from marshmallow.exceptions import ValidationError
from app.user.models.user import UserSchema, User
from app.user.user_validator import UserInputs
from . import bp
from flask import request, jsonify
from app import db,logger

user_schema = UserSchema()

@bp.route('', methods=['POST'])
def createUser():
    inputs = UserInputs(request)

    if not inputs.validate():
        return jsonify(success=False, errors=inputs.errors)
    
    json_data = request.get_json()
    if not json_data:
        return {"message": "No input data provided"}, 400
    # Validate and deserialize input
    try:
        data = user_schema.load(json_data)
    except ValidationError as err:
        return err.messages, 422

    u = User()
    u.firstName = data['firstName']
    u.lastName = data['lastName']
    u.email = data['email']
    u.phone = data['phone']
    u.username = data['username']

    db.session.add(u)
    db.session.commit()

    return "OK"

@bp.route('/<user_id>', methods=['GET'])
def getUser(user_id):
    logger.info('get user {}'.format(user_id))
    u = User.query.get(user_id)
    if not u:
        return jsonify({
            "code": 404,
            "message": "user not found"
        }), 404
    
    return jsonify(user_schema.dump(u))


@bp.route('/<user_id>', methods=['DELETE'])
def deleteUser(user_id):
    logger.info('delete user {}'.format(user_id))
    u = User.query.get(user_id)
    if not u:
        return jsonify({
            "code": 404,
            "message": "user not found"
        }), 404
    
    db.session.delete(u)
    db.session.commit()

    return "OK", 204

@bp.route('/<user_id>', methods=['PUT'])
def updateUser(user_id):
    logger.info('update user {}'.format(user_id))
    u = User.query.get(user_id)
    if not u:
        return jsonify({
            "code": 404,
            "message": "user not found"
        }), 404

    json_data = request.get_json()
    if not json_data:
        return {"message": "No input data provided"}, 400
    # Validate and deserialize input
    try:
        data = user_schema.load(json_data)
    except ValidationError as err:
        return err.messages, 422
    
    db.session.query(User).filter(User.id == user_id).update(data)
    db.session.commit()

    return "OK", 200