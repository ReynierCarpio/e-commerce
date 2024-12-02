"""empty message

Revision ID: f2g79061d441
Revises: e1f79061d440
Create Date: 2024-12-02 01:30:00
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f2g79061d441'
down_revision = 'e1f79061d440'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('product',
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('product_name', sa.String(length=100), nullable=False),
    sa.Column('seller_id', sa.Integer(), nullable=False),
    sa.Column('brand', sa.String(length=50), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('price', sa.Numeric(), nullable=False),
    sa.Column('stock', sa.Integer(), nullable=False),
    sa.Column('category_name', sa.String(length=100), nullable=False),
    sa.Column('sku', sa.String(length=50), nullable=True),
    sa.Column('image_url', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['seller_id'], ['seller.seller_id'], ),
    sa.PrimaryKeyConstraint('product_id')
    )


def downgrade():
    op.drop_table('product')
