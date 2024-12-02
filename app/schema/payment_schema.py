from marshmallow import Schema, fields

class PaymentSchema(Schema):
    payment_id = fields.Int(dump_only=True)
    order_id = fields.Int(required=True)
    total_amount = fields.Float(required=True)
    payment_method = fields.Str(required=True)
    payment_status = fields.Str(required=True)
    user_id = fields.Int(required=True)
    seller_id = fields.Int(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    deleted_at = fields.DateTime(dump_only=True)
