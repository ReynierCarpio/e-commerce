"""empty message

Revision ID: g3h79061d442
Revises: f2g79061d441
Create Date: 2024-12-02 01:35:10
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'g3h79061d442'
down_revision = 'f2g79061d441'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('order_item',
    sa.Column('order_item_id', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('seller_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('price', sa.Numeric(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['order.order_id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['product.product_id'], ),
    sa.ForeignKeyConstraint(['seller_id'], ['seller.seller_id'], ),
    sa.PrimaryKeyConstraint('order_item_id')
    )


def downgrade():
    op.drop_table('order_item')
