from flask_migrate import Migrate


# see: https://blog.csdn.net/qq_27366789/article/details/81665926
migrate = Migrate(render_as_batch=True)
