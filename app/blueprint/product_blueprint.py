from flask_smorest import Blueprint
from flask import abort, jsonify
from app.repository.product_repository import ProductRepository
from app.schema.product_schema import ProductSchema

product_blp = Blueprint("product", __name__, url_prefix="/products")

@product_blp.route("/", methods=["POST"])
@product_blp.arguments(ProductSchema)
@product_blp.response(201, ProductSchema)
def create_product(data):
    return ProductRepository.create_product(data)

@product_blp.route("/<int:product_id>", methods=["GET"])
@product_blp.response(200, ProductSchema)
def get_product_by_id(product_id):
    product = ProductRepository.get_product_by_id(product_id)
    if not product:
        abort(404, description="Product not found")
    return product

@product_blp.route("/", methods=["GET"])
@product_blp.response(200, ProductSchema(many=True))
def get_all_products():
    return ProductRepository.get_all_products()

@product_blp.route("/<int:product_id>", methods=["PUT"])
@product_blp.arguments(ProductSchema)
@product_blp.response(200, ProductSchema)
def update_product(data, product_id):
    product = ProductRepository.get_product_by_id(product_id)
    if not product:
        abort(404, description="Product not found")
    return ProductRepository.update_product(product, data)

@product_blp.route("/<int:product_id>", methods=["DELETE"])
@product_blp.response(204)
def delete_product(product_id):
    product = ProductRepository.get_product_by_id(product_id)
    if not product:
        abort(404, description="Product not found")
    ProductRepository.delete_product(product)
    return ""
