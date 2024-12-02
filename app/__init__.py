from flask import Flask, jsonify
from flask_smorest import Api

# Import blueprints
from app.blueprint.admin_blueprint import admin_blp
from app.blueprint.user_blueprint import user_blp
from app.blueprint.product_blueprint import product_blp
from app.blueprint.seller_blueprint import seller_blp
from app.blueprint.payment_blueprint import payment_blp
from app.blueprint.order_blueprint import order_blp
from app.blueprint.order_item_blueprint import order_item_blp
from app.blueprint.category_blueprint import category_blp
from app.blueprint.review_blueprint import review_blp
from app.extension import db, migrate
from config import Config
from app.models import admin_model
from app.models import user_model
from app.models import product_model
from app.models import seller_model
from app.models import payment_model
from app.models import order_model
from app.models import order_item_model
from app.models import category_model
from app.models import review_model

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Initialize API
    api = Api(app)

    # Register blueprints
    api.register_blueprint(admin_blp)
    api.register_blueprint(user_blp)
    api.register_blueprint(product_blp)
    api.register_blueprint(seller_blp)
    api.register_blueprint(payment_blp)
    api.register_blueprint(order_blp)
    api.register_blueprint(order_item_blp)
    api.register_blueprint(category_blp)
    api.register_blueprint(review_blp)

    # Create the database tables automatically
    with app.app_context():
        db.create_all()  # This will create all tables defined in models

    # Define a simple home route
    @app.route("/")
    def home():
        return jsonify({"message": "Welcome to the API!"})

    return app
