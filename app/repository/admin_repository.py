from app.extension import db
from app.models.admin_model import AdminModel
from datetime import datetime

class AdminRepository:
    @staticmethod
    def create_admin(data):
        admin = AdminModel(**data)
        db.session.add(admin)
        db.session.commit()
        return admin

    @staticmethod
    def get_admin_by_id(admin_id):
        return AdminModel.query.get(admin_id)

    @staticmethod
    def get_all_admins():
        return AdminModel.query.all()

    @staticmethod
    def update_admin(admin, data):
        for key, value in data.items():
            setattr(admin, key, value)
        db.session.commit()
        return admin

    @staticmethod
    def delete_admin(admin):
        admin.deleted_at = datetime.utcnow()
        db.session.commit()
