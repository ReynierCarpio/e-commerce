"""empty message

Revision ID: h4i79061d443
Revises: g3h79061d442
Create Date: 2024-12-02 01:40:00
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'h4i79061d443'
down_revision = 'g3h79061d442'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('payment',
    sa.Column('payment_id', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('total_amount', sa.Numeric(), nullable=False),
    sa.Column('payment_method', sa.Enum('Credit Card', 'Debit Card', 'PayPal', 'Bank Transfer', 'Crypto'), nullable=False),
    sa.Column('payment_status', sa.Enum('Pending', 'Completed', 'Failed', 'Refunded'), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('seller_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['order.order_id'], ),
    sa.ForeignKeyConstraint(['seller_id'], ['seller.seller_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('payment_id')
    )


def downgrade():
    op.drop_table('payment')
