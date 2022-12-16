from app import db


class Article(db.Model):
    __tablename__ = 'articles'
    create_at = db.Column(db.BigInteger)
    id = db.Column(db.Integer, primary_key=True)
    # the timestamp of an article modified
    modify_at = db.Column(db.BigInteger)
    # base info
    title = db.Column(db.String(128))
    author = db.Column(db.Integer, db.ForeignKey('users.id'))
    # tags =
    category = db.Column(db.Integer, db.ForeignKey('categories.id'))
    # more info
    cover = db.Column(db.Text)
    content = db.Column(db.Text)
    excerpt = db.Column(db.Text, nullable=True)
