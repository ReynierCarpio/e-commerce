from marshmallow import Schema, fields

class ProductSchema(Schema):
    product_id = fields.Int(dump_only=True)
    product_name = fields.Str(required=True)
    seller_id = fields.Int(required=True)
    brand = fields.Str()
    description = fields.Str()
    price = fields.Float(required=True)
    stock = fields.Int(required=True)
    category_name = fields.Str(required=True)
    sku = fields.Str()
    image_url = fields.Url()
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    deleted_at = fields.DateTime(dump_only=True)
