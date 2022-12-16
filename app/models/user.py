from werkzeug.security import generate_password_hash, check_password_hash

from app.extensions import db


class Permission:
    GENERAL = 0x01
    ADMINISTER = 0xff


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')

    @staticmethod
    def insert_roles():
        """
        insert roles when the role model was created
        :return: None
        """
        roles = {
            'User': (Permission.GENERAL,),
            'Administer': (Permission.ADMINISTER,)
        }

        # traverse the roles to insert everyone
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.permissions = roles[r][0]
            db.session.add(role)

    def __repr__(self):
        return '<Role \'%s\'>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(128))
    is_default = db.Column(db.Boolean, default=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    @property
    def password(self):
        raise AttributeError('`password` is not a readable attribute')

    @password.setter
    def password(self, passwd):
        self.password_hash = generate_password_hash(passwd)

    def verify_password(self, passwd):
        return check_password_hash(self.password_hash, passwd)
