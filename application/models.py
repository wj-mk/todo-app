from application import db

class Items(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30))
    description = db.Column(db.String(100), nullable = False)
    date = db.Column(db.DateTime)
    status = db.Column(db.Boolean, default = False)