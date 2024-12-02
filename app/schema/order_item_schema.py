from marshmallow import Schema, fields

class OrderItemSchema(Schema):
    order_item_id = fields.Int(dump_only=True)
    order_id = fields.Int(required=True)
    product_id = fields.Int(required=True)
    seller_id = fields.Int(required=True)
    quantity = fields.Int(required=True)
    price = fields.Float(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    deleted_at = fields.DateTime(dump_only=True)
