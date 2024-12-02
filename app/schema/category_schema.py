from marshmallow import Schema, fields

class CategorySchema(Schema):
    category_id = fields.Int(dump_only=True)
    category_name = fields.Str(required=True)
    description = fields.Str()
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    deleted_at = fields.DateTime(dump_only=True)
