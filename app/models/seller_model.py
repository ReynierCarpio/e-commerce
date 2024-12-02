from app.extension import db

class SellerModel(db.Model):
    __tablename__ = "seller"

    seller_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    business_name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    deleted_at = db.Column(db.DateTime, nullable=True)

    products = db.relationship("ProductModel", backref="seller", lazy=True)
    payments = db.relationship("PaymentModel", backref="seller", lazy=True)
    reviews = db.relationship("ReviewModel", backref="seller", lazy=True)
    orders = db.relationship("OrderModel", backref="seller", lazy=True)
    order_items = db.relationship("OrderItemModel", backref="seller", lazy=True)
