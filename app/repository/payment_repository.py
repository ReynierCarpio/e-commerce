from app.extension import db
from app.models.payment_model import PaymentModel
from datetime import datetime

class PaymentRepository:
    @staticmethod
    def create_payment(data):
        payment = PaymentModel(**data)
        db.session.add(payment)
        db.session.commit()
        return payment

    @staticmethod
    def get_payment_by_id(payment_id):
        return PaymentModel.query.get(payment_id)

    @staticmethod
    def get_all_payments():
        return PaymentModel.query.filter_by(deleted_at=None).all()

    @staticmethod
    def update_payment(payment, data):
        for key, value in data.items():
            setattr(payment, key, value)
        db.session.commit()
        return payment

    @staticmethod
    def delete_payment(payment):
        payment.deleted_at = datetime.utcnow()
        db.session.commit()
