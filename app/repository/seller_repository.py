from app.extension import db
from app.models.seller_model import SellerModel
from datetime import datetime

class SellerRepository:
    @staticmethod
    def create_seller(data):
        seller = SellerModel(**data)
        db.session.add(seller)
        db.session.commit()
        return seller

    @staticmethod
    def get_seller_by_id(seller_id):
        return SellerModel.query.get(seller_id)

    @staticmethod
    def get_all_sellers():
        return SellerModel.query.filter_by(deleted_at=None).all()

    @staticmethod
    def update_seller(seller, data):
        for key, value in data.items():
            setattr(seller, key, value)
        db.session.commit()
        return seller

    @staticmethod
    def delete_seller(seller):
        seller.deleted_at = datetime.utcnow()
        db.session.commit()
