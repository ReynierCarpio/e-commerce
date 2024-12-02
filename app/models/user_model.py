from app.extension import db

class UserModel(db.Model):
    __tablename__ = "user"

    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    deleted_at = db.Column(db.DateTime, nullable=True)

    reviews = db.relationship("ReviewModel", backref="user", lazy=True)
    orders = db.relationship("OrderModel", backref="user", lazy=True)
    payments = db.relationship("PaymentModel", backref="user", lazy=True)
