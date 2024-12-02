from marshmallow import Schema, fields

class UserSchema(Schema):
    user_id = fields.Int(dump_only=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True, load_only=True)
    name = fields.Str(required=True)
    address = fields.Str(required=True)
    phone_number = fields.Str(required=True)
    role = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    deleted_at = fields.DateTime(dump_only=True)
