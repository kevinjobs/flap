from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import inspect

from app.extensions.db import db
from app.utils.moment import now_timestamp
from app.utils.short_uuid import short_uuid


class User(db.Model):
    __tablename__ = 'users'
    create_at = db.Column(db.BigInteger, default=now_timestamp())
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(8), default=short_uuid)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(128))
    is_default = db.Column(db.Boolean, default=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    articles = db.relationship('Article', backref='users', lazy='dynamic')

    def to_dict(self):
        data = {
            c.key:
                getattr(self, c.key) for c in inspect(self).mapper.column_attrs
        }
        del data['password_hash']
        # del data['role_id']
        return data

    @property
    def password(self):
        raise AttributeError('`password` is not a readable attribute')

    @password.setter
    def password(self, passwd):
        self.password_hash = generate_password_hash(passwd)

    def verify_password(self, passwd):
        return check_password_hash(self.password_hash, passwd)
