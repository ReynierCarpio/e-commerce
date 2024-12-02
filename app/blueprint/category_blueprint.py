from flask_smorest import Blueprint
from flask import abort
from app.repository.category_repository import CategoryRepository
from app.schema.category_schema import CategorySchema

category_blp = Blueprint("category", __name__, url_prefix="/categories")

@category_blp.route("/", methods=["POST"])
@category_blp.arguments(CategorySchema)
@category_blp.response(201, CategorySchema)
def create_category(data):
    return CategoryRepository.create_category(data)

@category_blp.route("/<int:category_id>", methods=["GET"])
@category_blp.response(200, CategorySchema)
def get_category_by_id(category_id):
    category = CategoryRepository.get_category_by_id(category_id)
    if not category:
        abort(404, description="Category not found")
    return category

@category_blp.route("/", methods=["GET"])
@category_blp.response(200, CategorySchema(many=True))
def get_all_categories():
    return CategoryRepository.get_all_categories()

@category_blp.route("/<int:category_id>", methods=["PUT"])
@category_blp.arguments(CategorySchema)
@category_blp.response(200, CategorySchema)
def update_category(data, category_id):
    category = CategoryRepository.get_category_by_id(category_id)
    if not category:
        abort(404, description="Category not found")
    return CategoryRepository.update_category(category, data)

@category_blp.route("/<int:category_id>", methods=["DELETE"])
@category_blp.response(204)
def delete_category(category_id):
    category = CategoryRepository.get_category_by_id(category_id)
    if not category:
        abort(404, description="Category not found")
    CategoryRepository.delete_category(category)
    return ""
