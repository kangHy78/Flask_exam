from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Text(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)