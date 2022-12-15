from flask import Blueprint


auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.get('/')
def index():
    return '<p>auth home page</p>'
