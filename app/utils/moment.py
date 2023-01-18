import time


def now_timestamp():
    """linux timestamp(15) of now
    """
    return int(time.time()*1000)
