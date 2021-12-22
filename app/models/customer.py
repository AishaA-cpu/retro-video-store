from app import db



class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    phone  = db.Column(db.String, nullable=False)
    registered_at = db.Column(db.DateTime)
    postal_code = db.Column(db.String)
