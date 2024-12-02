from flask_smorest import Blueprint
from flask import abort
from app.repository.payment_repository import PaymentRepository
from app.schema.payment_schema import PaymentSchema

payment_blp = Blueprint("payment", __name__, url_prefix="/payments")

@payment_blp.route("/", methods=["POST"])
@payment_blp.arguments(PaymentSchema)
@payment_blp.response(201, PaymentSchema)
def create_payment(data):
    return PaymentRepository.create_payment(data)

@payment_blp.route("/<int:payment_id>", methods=["GET"])
@payment_blp.response(200, PaymentSchema)
def get_payment_by_id(payment_id):
    payment = PaymentRepository.get_payment_by_id(payment_id)
    if not payment:
        abort(404, description="Payment not found")
    return payment

@payment_blp.route("/", methods=["GET"])
@payment_blp.response(200, PaymentSchema(many=True))
def get_all_payments():
    return PaymentRepository.get_all_payments()

@payment_blp.route("/<int:payment_id>", methods=["PUT"])
@payment_blp.arguments(PaymentSchema)
@payment_blp.response(200, PaymentSchema)
def update_payment(data, payment_id):
    payment = PaymentRepository.get_payment_by_id(payment_id)
    if not payment:
        abort(404, description="Payment not found")
    return PaymentRepository.update_payment(payment, data)

@payment_blp.route("/<int:payment_id>", methods=["DELETE"])
@payment_blp.response(204)
def delete_payment(payment_id):
    payment = PaymentRepository.get_payment_by_id(payment_id)
    if not payment:
        abort(404, description="Payment not found")
    PaymentRepository.delete_payment(payment)
    return ""
