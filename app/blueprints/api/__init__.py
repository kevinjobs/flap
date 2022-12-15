from flask import Blueprint


api = Blueprint('api', __name__, url_prefix='/api')


@api.get('/version')
def get_version():
    return {
        'version': 1,
        'update_at': '2022-12-15'
    }
