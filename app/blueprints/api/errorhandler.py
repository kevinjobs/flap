from app.blueprints.api import api
from app.utils import resp, RespCode


@api.errorhandler(Exception)
def intergrity_error(error):
    return resp(RespCode.ERROR, 'insert data failed.')
