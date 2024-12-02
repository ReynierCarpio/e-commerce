from app.extension import db

class PaymentModel(db.Model):
    __tablename__ = "payment"

    payment_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("order.order_id"), nullable=False)
    total_amount = db.Column(db.Numeric, nullable=False)
    payment_method = db.Column(db.Enum("Credit Card", "Debit Card", "PayPal", "Bank Transfer", "Crypto"), nullable=False)
    payment_status = db.Column(db.Enum("Pending", "Completed", "Failed", "Refunded"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)
    seller_id = db.Column(db.Integer, db.ForeignKey("seller.seller_id"), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    deleted_at = db.Column(db.DateTime, nullable=True)
