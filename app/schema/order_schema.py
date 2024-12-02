from marshmallow import Schema, fields

class OrderSchema(Schema):
    order_id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    seller_id = fields.Int(required=True)
    total_amount = fields.Float(required=True)
    order_status = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    deleted_at = fields.DateTime(dump_only=True)
