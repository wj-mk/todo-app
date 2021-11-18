from application import db
from datetime import date

class Items(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30))
    desc = db.Column(db.String(100))
    date = db.Column(db.DateTime, default=date.today())
    status = db.Column(db.String(5), default = 'todo')

db.create_all()