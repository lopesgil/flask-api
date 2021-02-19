from quotr import db

class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    code = db.Column(db.String(3), index=True, unique=True)
    users = db.relationship('User', backref='country', lazy='dynamic')

    def __repr__(self):
        return '<Country {}>'.format(self.name)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120),index=True, unique=True)
    password_hash = db.Column(db.String(128))
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))

    def __repr__(self):
        return '<User {}>'.format(self.username)
