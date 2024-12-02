from app.extension import db
from app.models.order_item_model import OrderItemModel
from datetime import datetime

class OrderItemRepository:
    @staticmethod
    def create_order_item(data):
        order_item = OrderItemModel(**data)
        db.session.add(order_item)
        db.session.commit()
        return order_item

    @staticmethod
    def get_order_item_by_id(order_item_id):
        return OrderItemModel.query.get(order_item_id)

    @staticmethod
    def get_all_order_items():
        return OrderItemModel.query.filter_by(deleted_at=None).all()

    @staticmethod
    def update_order_item(order_item, data):
        for key, value in data.items():
            setattr(order_item, key, value)
        db.session.commit()
        return order_item

    @staticmethod
    def delete_order_item(order_item):
        order_item.deleted_at = datetime.utcnow()
        db.session.commit()
