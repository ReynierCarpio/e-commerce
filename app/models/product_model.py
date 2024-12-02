from app.extension import db

class ProductModel(db.Model):
    __tablename__ = "product"

    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    seller_id = db.Column(db.Integer, db.ForeignKey("seller.seller_id"), nullable=False)
    brand = db.Column(db.String(50))
    description = db.Column(db.String(255))
    price = db.Column(db.Numeric, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    category_name = db.Column(db.String(100), nullable=False)
    sku = db.Column(db.String(50))
    image_url = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    deleted_at = db.Column(db.DateTime, nullable=True)

    reviews = db.relationship("ReviewModel", backref="product", lazy=True)
    order_items = db.relationship("OrderItemModel", backref="product", lazy=True)
