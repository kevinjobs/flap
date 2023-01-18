class UserError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)


class UserDoesntExistError(UserError):
    def __init__(self):
        super().__init__('user doesn\'t exist.')
