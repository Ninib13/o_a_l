from app import db

class User(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    username = db.Column(db.String(256), index=True, unique=True)
    firstName = db.Column(db.String(256))
    lastName = db.Column(db.String(256))
    email = db.Column(db.String(256), index=True, unique=True)
    phone = db.Column(db.String(256))

    def __repr__(self) -> str:
        return '{ id: {}, username: {}}'.format(self.id, self.username)