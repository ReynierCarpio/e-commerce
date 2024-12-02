"""empty message

Revision ID: e1f79061d440
Revises: d0e79061d439
Create Date: 2024-12-02 01:25:45
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1f79061d440'
down_revision = 'd0e79061d439'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('order',
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('seller_id', sa.Integer(), nullable=False),
    sa.Column('total_amount', sa.Numeric(), nullable=False),
    sa.Column('order_status', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['seller_id'], ['seller.seller_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('order_id')
    )


def downgrade():
    op.drop_table('order')
