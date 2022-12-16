import time


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


def now_timestamp():
    """linux timestamp(15) of now
    """
    return int(time.time()*1000)
