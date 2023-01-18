from app.blueprints.api import api
from app.utils import resp, RespCode
from sqlalchemy.exc import \
    IntegrityError, NoSuchTableError, SQLAlchemyError, NoResultFound


@api.errorhandler(500)
def internal_server_error(error):
    return resp(RespCode.ERROR, 'internal server error.')


@api.errorhandler(IntegrityError)
def intergrity_error(error):
    return resp(RespCode.ERROR, 'insert data failed.')


@api.errorhandler(NoSuchTableError)
def no_such_table(error):
    return resp(RespCode.ERROR, 'no such table.')


@api.errorhandler(SQLAlchemyError)
def sqlalchemy_error(error):
    return resp(RespCode.ERROR, 'database error.')


@api.errorhandler(NoResultFound)
def no_result_found(error):
    return resp(RespCode.ERROR, 'no result found.')
