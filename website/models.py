from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from . import db



class User(db.Model, UserMixin):
    __tablename__= "users"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    location = db.Column(db.String(150), nullable=False)
    date_created = db.Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
