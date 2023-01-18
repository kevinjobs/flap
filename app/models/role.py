from app import db
from app.utils import now_timestamp


class Permission:
    GENERAL = 0x01
    ADMINISTER = 0xff


class Role(db.Model):
    __tablename__ = 'roles'
    create_at = db.Column(db.BigInteger, default=now_timestamp())
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='roles', lazy='dynamic')

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
