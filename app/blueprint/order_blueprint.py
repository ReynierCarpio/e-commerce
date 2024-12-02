from flask_smorest import Blueprint
from flask import abort
from app.repository.order_repository import OrderRepository
from app.schema.order_schema import OrderSchema

order_blp = Blueprint("order", __name__, url_prefix="/orders")

@order_blp.route("/", methods=["POST"])
@order_blp.arguments(OrderSchema)
@order_blp.response(201, OrderSchema)
def create_order(data):
    return OrderRepository.create_order(data)

@order_blp.route("/<int:order_id>", methods=["GET"])
@order_blp.response(200, OrderSchema)
def get_order_by_id(order_id):
    order = OrderRepository.get_order_by_id(order_id)
    if not order:
        abort(404, description="Order not found")
    return order

@order_blp.route("/", methods=["GET"])
@order_blp.response(200, OrderSchema(many=True))
def get_all_orders():
    return OrderRepository.get_all_orders()

@order_blp.route("/<int:order_id>", methods=["PUT"])
@order_blp.arguments(OrderSchema)
@order_blp.response(200, OrderSchema)
def update_order(data, order_id):
    order = OrderRepository.get_order_by_id(order_id)
    if not order:
        abort(404, description="Order not found")
    return OrderRepository.update_order(order, data)

@order_blp.route("/<int:order_id>", methods=["DELETE"])
@order_blp.response(204)
def delete_order(order_id):
    order = OrderRepository.get_order_by_id(order_id)
    if not order:
        abort(404, description="Order not found")
    OrderRepository.delete_order(order)
    return ""
