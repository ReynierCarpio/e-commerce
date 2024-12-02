from flask_smorest import Blueprint
from flask import abort, jsonify
from app.repository.admin_repository import AdminRepository
from app.schema.admin_schema import AdminSchema

admin_blp = Blueprint("admin", __name__, url_prefix="/admin")

@admin_blp.route("/", methods=["POST"])
@admin_blp.arguments(AdminSchema)
@admin_blp.response(201, AdminSchema)
def create_admin(data):
    admin = AdminRepository.create_admin(data)
    return admin

@admin_blp.route("/<int:admin_id>", methods=["GET"])
@admin_blp.response(200, AdminSchema)
def get_admin_by_id(admin_id):
    admin = AdminRepository.get_admin_by_id(admin_id)
    if not admin:
        abort(404, description="Admin not found")
    return admin

@admin_blp.route("/", methods=["GET"])
@admin_blp.response(200, AdminSchema(many=True))
def get_all_admins():
    return AdminRepository.get_all_admins()

@admin_blp.route("/<int:admin_id>", methods=["PUT"])
@admin_blp.arguments(AdminSchema)
@admin_blp.response(200, AdminSchema)
def update_admin(data, admin_id):
    admin = AdminRepository.get_admin_by_id(admin_id)
    if not admin:
        abort(404, description="Admin not found")
    return AdminRepository.update_admin(admin, data)

@admin_blp.route("/<int:admin_id>", methods=["DELETE"])
@admin_blp.response(204)
def delete_admin(admin_id):
    admin = AdminRepository.get_admin_by_id(admin_id)
    if not admin:
        abort(404, description="Admin not found")
    AdminRepository.delete_admin(admin)
    return ""
