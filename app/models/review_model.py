from app.extension import db

class ReviewModel(db.Model):
    __tablename__ = "review"

    review_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("product.product_id"), nullable=False)
    seller_id = db.Column(db.Integer, db.ForeignKey("seller.seller_id"), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    deleted_at = db.Column(db.DateTime, nullable=True)
