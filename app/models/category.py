from app.extensions.db import db
from app.utils import now_timestamp


class Category(db.Model):
    __tablename__ = 'categories'
    create_at = db.Column(db.BigInteger, default=now_timestamp())
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    articles = db.relationship('Article', backref='categories', lazy='dynamic')
