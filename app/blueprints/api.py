from flask import Blueprint
from sqlalchemy.exc import IntegrityError

from app import db
from app.models import User
from app.utils import resp, RespCode


api = Blueprint('api', __name__, url_prefix='/api')


@api.get('/version')
def get_version():
    return {
        'version': 1,
        'update_at': '2022-12-15'
    }


@api.post('/register')
def add_new():
    user = User(
        name='KevinJobs',
        email='me@kevinjobs.com',
        password='june1995'
    )
    db.session.add(user)
    try:
        db.session.commit()
    except IntegrityError:
        return resp(RespCode.ERROR, 'user existed')

    return resp(RespCode.OK, 'add new user success')
