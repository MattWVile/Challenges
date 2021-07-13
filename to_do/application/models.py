from application import db

class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    # done = db.Column(db.Boolean, nullable=False, default = False)