"""empty message

Revision ID: i5j79061d444
Revises: h4i79061d443
Create Date: 2024-12-02 01:45:25
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'i5j79061d444'
down_revision = 'h4i79061d443'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('review',
    sa.Column('review_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('seller_id', sa.Integer(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product.product_id'], ),
    sa.ForeignKeyConstraint(['seller_id'], ['seller.seller_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('review_id')
    )


def downgrade():
    op.drop_table('review')
