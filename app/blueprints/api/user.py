from flask import request

from app import db
from app.exceptions import UserDoesntExist
from app.models import User
from app.utils import resp, RespCode
from app.blueprints.api.create_blueprint import api


@api.get('/users')
def get_user_list():
    users = User.query.all()
    return resp(
        RespCode.OK,
        'get user list success',
        [u.to_dict() for u in users]
    )


@api.post('/user')
def add_new_user():
    name, email, password = \
        request.form.get('name'), \
        request.form.get('email'), \
        request.form.get('password')

    user = User(name=name, email=email, password=password)
    db.session.add(user)
    db.session.commit()
    new_user = User.query.filter(User.name == request.form.get('name')).one()
    return resp(RespCode.OK, 'add new user success', new_user.to_dict())


@api.get('/user/<username>')
def get_user_by_name(username):
    users = User.query.filter(User.name == username).all()
    if not users:
        raise UserDoesntExist
    return resp(
        RespCode.OK,
        'get user success',
        [user.to_dict() for user in users]
    )


@api.delete('/user/<email>')
def delete_user_by_email(email):
    result = User.query.filter(User.email == email).one()
    if not result:
        raise UserDoesntExist
    db.session.delete(result)
    db.session.commit()
    return resp(RespCode.OK, 'delete user sucecss')
