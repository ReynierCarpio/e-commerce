from flask_smorest import Blueprint
from flask import abort
from app.repository.review_repository import ReviewRepository
from app.schema.review_schema import ReviewSchema

review_blp = Blueprint("review", __name__, url_prefix="/reviews")

@review_blp.route("/", methods=["POST"])
@review_blp.arguments(ReviewSchema)
@review_blp.response(201, ReviewSchema)
def create_review(data):
    return ReviewRepository.create_review(data)

@review_blp.route("/<int:review_id>", methods=["GET"])
@review_blp.response(200, ReviewSchema)
def get_review_by_id(review_id):
    review = ReviewRepository.get_review_by_id(review_id)
    if not review:
        abort(404, description="Review not found")
    return review

@review_blp.route("/", methods=["GET"])
@review_blp.response(200, ReviewSchema(many=True))
def get_all_reviews():
    return ReviewRepository.get_all_reviews()

@review_blp.route("/<int:review_id>", methods=["PUT"])
@review_blp.arguments(ReviewSchema)
@review_blp.response(200, ReviewSchema)
def update_review(data, review_id):
    review = ReviewRepository.get_review_by_id(review_id)
    if not review:
        abort(404, description="Review not found")
    return ReviewRepository.update_review(review, data)

@review_blp.route("/<int:review_id>", methods=["DELETE"])
@review_blp.response(204)
def delete_review(review_id):
    review = ReviewRepository.get_review_by_id(review_id)
    if not review:
        abort(404, description="Review not found")
    ReviewRepository.delete_review(review)
    return ""
