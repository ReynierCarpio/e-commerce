from app.extension import db
from app.models.product_model import ProductModel
from datetime import datetime

class ProductRepository:
    @staticmethod
    def create_product(data):
        product = ProductModel(**data)
        db.session.add(product)
        db.session.commit()
        return product

    @staticmethod
    def get_product_by_id(product_id):
        return ProductModel.query.get(product_id)

    @staticmethod
    def get_all_products():
        return ProductModel.query.filter_by(deleted_at=None).all()

    @staticmethod
    def update_product(product, data):
        for key, value in data.items():
            setattr(product, key, value)
        db.session.commit()
        return product

    @staticmethod
    def delete_product(product):
        product.deleted_at = datetime.utcnow()
        db.session.commit()
