from app.extension import db
from app.models.category_model import CategoryModel
from datetime import datetime

class CategoryRepository:
    @staticmethod
    def create_category(data):
        category = CategoryModel(**data)
        db.session.add(category)
        db.session.commit()
        return category

    @staticmethod
    def get_category_by_id(category_id):
        return CategoryModel.query.get(category_id)

    @staticmethod
    def get_all_categories():
        return CategoryModel.query.filter_by(deleted_at=None).all()

    @staticmethod
    def update_category(category, data):
        for key, value in data.items():
            setattr(category, key, value)
        db.session.commit()
        return category

    @staticmethod
    def delete_category(category):
        category.deleted_at = datetime.utcnow()
        db.session.commit()
