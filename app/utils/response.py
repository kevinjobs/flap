from enum import IntEnum, unique


@unique
class RespCode(IntEnum):
    OK = 0
    ERROR = 1
    UNAUTHORIZED = 4001
    NOT_FOUND = 4004
    INTERNAL_SERVER_ERROR = 5001
    SERVICE_UNAVAILABLE = 5003


def resp(code, msg, data=None):
    result = {
        'code': code,
        'msg': msg,
    }

    if data is not None:
        result['data'] = data

    return result
