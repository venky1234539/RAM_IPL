
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Ferry(db.Model):
    # __tablename__ = "star"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), nullable = False)
    age = db.Column(db.Integer, nullable = False)




















