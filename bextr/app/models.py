from app import db


class Subscriber(db.Model):
    __tablename__ = 'subscribers'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    epoch = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(200), index=True, unique=True)
