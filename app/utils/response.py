class RespCode:
    OK = 0
    ERROR = 1


def resp(code, msg, data=None):
    result = {
        'code': code,
        'msg': msg,
    }

    if data is not None:
        result['data'] = data

    return result
