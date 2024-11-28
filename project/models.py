from flask_sqlalchemy import SQLAlchemy

from flask import Flask

app = Flask('__name__')


app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testpmk.db'

db = SQLAlchemy(app)


class user(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    id_auth = db.Column(db.Integer)
    id_project = db.Column(db.Integer)
    id_social = db.Column(db.Integer)
    email = db.Column(db.String(100))
    phone_number= db.Column(db.Integer)
    first_name = db.Column(db.String(100))
class auth(db.Model):
    __tablename__ = 'auth'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(20))
    password = db.Column(db.String(20))
class skills(db.Model):
    __tablename__ = 'skills'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer)
    id_user = db.Column(db.Integer)
    id_type = db.Column(db.Integer)
class social(db.Model):
    __tablename__ = 'social'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer)
    id_user = db.Column(db.Integer)
    id_type_social = db.Column(db.Integer)
class type_social(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    __tablename__ = 'type_social'
    name = db.Column(db.String(30))
class type_skills(db.Model):
    __tablename__ = 'type_skills'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
class projects(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    id_review = db.Column(db.Integer)
    url = db.Column(db.String(100))
class reviews(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    user =  db.Column(db.String(50), unique=True, nullable=False)
    review = db.Column(db.String(100))


with app.app_context():

    db.session.commit()

    db.create_all()