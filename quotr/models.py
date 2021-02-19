from quotr import db

class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, nullable=False)
    code = db.Column(db.String(3), index=True, unique=True, nullable=False)
    users = db.relationship('User', backref='country', lazy='dynamic')

    def __repr__(self):
        return '<Country {}>'.format(self.name)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120),index=True, unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))
    quotes = db.relationship('FavoriteQuote',
                             backref='user',
                             lazy='dynamic',
                             cascade='all, delete')

    def __repr__(self):
        return '<User {}>'.format(self.username)

class FavoriteQuote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(128), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '<Quote "{}">'.format(self.body)
