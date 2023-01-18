from flask import Blueprint, request

from app import db
from app.exceptions import UserDoesntExistError
from app.models import User, Article
from app.utils import resp, RespCode


api = Blueprint('api', __name__)


@api.post('/register')
def add_new():
    user = User(
        name=request.form.get('name'),
        email=request.form.get('email'),
        password=request.form.get('password')
    )
    db.session.add(user)
    db.session.commit()
    return resp(RespCode.OK, 'add new user success')


@api.get('/users')
def get_user_list():
    users = User.query.all()
    return resp(
        RespCode.OK,
        'get user list success',
        [u.to_dict() for u in users]
    )


@api.get('/user/<username>')
def get_user_by_name(username):
    user = User.query.filter(User.name == username).all()
    if not user:
        raise UserDoesntExistError
    return resp(RespCode.OK, 'get user success', user.to_dict())


@api.delete('/user/<user_id>')
def delete_user_by_id(user_id):
    result = User.query.filter(User.id == int(user_id)).one()
    db.session.delete(result)
    db.session.commit()
    return resp(RespCode.OK, 'remove user sucecss')


@api.get('/articles')
def get_article_list():
    articles = Article.query.all()
    return resp(
        RespCode.OK,
        'get article list success',
        [a.to_dict() for a in articles]
    )
