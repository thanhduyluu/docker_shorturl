import datetime

from model.config import db


class URL(db.Model):
    __tablename__ = "cv1805_short_URL"

    id = db.Column('id', db.Integer, primary_key=True, unique=True, autoincrement=True)

    shortToken = db.Column('short_token', db.String(50), unique=True, index=True)

    longURL = db.Column('long_URL', db.String(500))

    userEmail = db.Column('user_email', db.String(50))  # userID can null

    status = db.Column('status', db.String(50))

    creatAt = db.Column('create_at', db.DateTime)

    expireAt = db.Column('expire_at', db.DateTime)

    column1 = db.Column("column_1", db.String(50))

    column2 = db.Column("column_2", db.String(50))

    column3 = db.Column("column_3", db.String(50),index=True)

    column4 = db.Column("column_4",db.String(50),index=True)

    column5 = db.Column("column_5", db.Integer)

    column6 = db.Column("column_6", db.Integer)

    column7 = db.Column("column_7", db.DateTime)

    column8 = db.Column("column_8", db.DateTime)

    column9 = db.Column("column_9", db.String(50))

    column10 = db.Column("column_10", db.String(50))

    def __init__(self, shortToken, longToken, creatAt, expireAt):

        self.shortToken = shortToken

        self.longURL = longToken

        self.userId = None

        self.status = "on"

        self.creatAt = creatAt

        self.expireAt = expireAt

        self.userEmail = None

        self.column1 = None

        self.column2 = None

        self.column3 = None

        self.column4 = None

        self.column5 = None

        self.column6 = None

        self.column7 = None

        self.column8 = None

        self.column9 = None

        self.column10 = None
