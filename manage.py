import os
from flask_script import Manager, Server

from app import create_app


app = create_app(os.getenv('FLASK_CONFIG'))
manager = Manager(app)

# add a command
manager.add_command('run', Server(host='localhost'))


# add a conmmand via decorator
@manager.command
def lift():
    print("hello, flask!")


if __name__ == "__main__":
    manager.run()

# question: No module named flask._compat
# see: https://blog.csdn.net/eagle5063/article/details/126995069
