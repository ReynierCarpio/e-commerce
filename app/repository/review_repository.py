from app.extension import db
from app.models.review_model import ReviewModel
from datetime import datetime

class ReviewRepository:
    @staticmethod
    def create_review(data):
        review = ReviewModel(**data)
        db.session.add(review)
        db.session.commit()
        return review

    @staticmethod
    def get_review_by_id(review_id):
        return ReviewModel.query.get(review_id)

    @staticmethod
    def get_all_reviews():
        return ReviewModel.query.filter_by(deleted_at=None).all()

    @staticmethod
    def update_review(review, data):
        for key, value in data.items():
            setattr(review, key, value)
        db.session.commit()
        return review

    @staticmethod
    def delete_review(review):
        review.deleted_at = datetime.utcnow()
        db.session.commit()
