from flask_smorest import Blueprint
from flask import abort
from app.repository.seller_repository import SellerRepository
from app.schema.seller_schema import SellerSchema

seller_blp = Blueprint("seller", __name__, url_prefix="/sellers")

@seller_blp.route("/", methods=["POST"])
@seller_blp.arguments(SellerSchema)
@seller_blp.response(201, SellerSchema)
def create_seller(data):
    return SellerRepository.create_seller(data)

@seller_blp.route("/<int:seller_id>", methods=["GET"])
@seller_blp.response(200, SellerSchema)
def get_seller_by_id(seller_id):
    seller = SellerRepository.get_seller_by_id(seller_id)
    if not seller:
        abort(404, description="Seller not found")
    return seller

@seller_blp.route("/", methods=["GET"])
@seller_blp.response(200, SellerSchema(many=True))
def get_all_sellers():
    return SellerRepository.get_all_sellers()

@seller_blp.route("/<int:seller_id>", methods=["PUT"])
@seller_blp.arguments(SellerSchema)
@seller_blp.response(200, SellerSchema)
def update_seller(data, seller_id):
    seller = SellerRepository.get_seller_by_id(seller_id)
    if not seller:
        abort(404, description="Seller not found")
    return SellerRepository.update_seller(seller, data)

@seller_blp.route("/<int:seller_id>", methods=["DELETE"])
@seller_blp.response(204)
def delete_seller(seller_id):
    seller = SellerRepository.get_seller_by_id(seller_id)
    if not seller:
        abort(404, description="Seller not found")
    SellerRepository.delete_seller(seller)
    return ""
