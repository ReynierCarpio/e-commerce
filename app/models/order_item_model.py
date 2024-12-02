from app.extension import db

class OrderItemModel(db.Model):
    __tablename__ = "order_item"

    order_item_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("order.order_id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("product.product_id"), nullable=False)
    seller_id = db.Column(db.Integer, db.ForeignKey("seller.seller_id"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    deleted_at = db.Column(db.DateTime, nullable=True)
