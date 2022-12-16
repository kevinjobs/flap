from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError

from app import db
from app.models import User
from app.utils import resp, RespCode


api = Blueprint('api', __name__)


@api.get('/version')
def get_version():
    return {
        'version': 1,
        'update_at': '2022-12-15'
    }


@api.post('/register')
def add_new():
    user = User(
        name=request.form.get('name'),
        email=request.form.get('email'),
        password=request.form.get('password')
    )
    db.session.add(user)
    try:
        db.session.commit()
        return resp(RespCode.OK, 'add new user success')
    except IntegrityError:
        return resp(RespCode.ERROR, 'user existed')


@api.get('/users')
def get_user_list():
    user = User.query.all()
    return resp(RespCode.OK, 'get user list success', user)
