from flask_smorest import Blueprint
from flask import abort
from app.repository.order_item_repository import OrderItemRepository
from app.schema.order_item_schema import OrderItemSchema

order_item_blp = Blueprint("order_item", __name__, url_prefix="/order-items")

@order_item_blp.route("/", methods=["POST"])
@order_item_blp.arguments(OrderItemSchema)
@order_item_blp.response(201, OrderItemSchema)
def create_order_item(data):
    return OrderItemRepository.create_order_item(data)

@order_item_blp.route("/<int:order_item_id>", methods=["GET"])
@order_item_blp.response(200, OrderItemSchema)
def get_order_item_by_id(order_item_id):
    order_item = OrderItemRepository.get_order_item_by_id(order_item_id)
    if not order_item:
        abort(404, description="Order item not found")
    return order_item

@order_item_blp.route("/", methods=["GET"])
@order_item_blp.response(200, OrderItemSchema(many=True))
def get_all_order_items():
    return OrderItemRepository.get_all_order_items()

@order_item_blp.route("/<int:order_item_id>", methods=["PUT"])
@order_item_blp.arguments(OrderItemSchema)
@order_item_blp.response(200, OrderItemSchema)
def update_order_item(data, order_item_id):
    order_item = OrderItemRepository.get_order_item_by_id(order_item_id)
    if not order_item:
        abort(404, description="Order item not found")
    return OrderItemRepository.update_order_item(order_item, data)

@order_item_blp.route("/<int:order_item_id>", methods=["DELETE"])
@order_item_blp.response(204)
def delete_order_item(order_item_id):
    order_item = OrderItemRepository.get_order_item_by_id(order_item_id)
    if not order_item:
        abort(404, description="Order item not found")
    OrderItemRepository.delete_order_item(order_item)
    return ""
