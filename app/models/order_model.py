from app.extension import db

class OrderModel(db.Model):
    __tablename__ = "order"

    order_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)
    seller_id = db.Column(db.Integer, db.ForeignKey("seller.seller_id"), nullable=False)
    total_amount = db.Column(db.Numeric, nullable=False)
    order_status = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    deleted_at = db.Column(db.DateTime, nullable=True)

    order_items = db.relationship("OrderItemModel", backref="order", lazy=True)
    payment = db.relationship("PaymentModel", backref="order", uselist=False)
