from app import db


class Category(db.Model):
    __tablename__ = 'categories'
    create_at = db.Column(db.BigInteger)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    articles = db.relationship('Article', backref='category', lazy='dynamic')
