from app.extension import db
from app.models.order_model import OrderModel
from datetime import datetime

class OrderRepository:
    @staticmethod
    def create_order(data):
        order = OrderModel(**data)
        db.session.add(order)
        db.session.commit()
        return order

    @staticmethod
    def get_order_by_id(order_id):
        return OrderModel.query.get(order_id)

    @staticmethod
    def get_all_orders():
        return OrderModel.query.filter_by(deleted_at=None).all()

    @staticmethod
    def update_order(order, data):
        for key, value in data.items():
            setattr(order, key, value)
        db.session.commit()
        return order

    @staticmethod
    def delete_order(order):
        order.deleted_at = datetime.utcnow()
        db.session.commit()
