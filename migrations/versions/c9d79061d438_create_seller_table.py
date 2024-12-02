"""empty message

Revision ID: c9d79061d438
Revises: b8c79061d437
Create Date: 2024-12-02 01:18:30
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c9d79061d438'
down_revision = 'b8c79061d437'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('seller',
    sa.Column('seller_id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('phone', sa.String(length=15), nullable=False),
    sa.Column('business_name', sa.String(length=100), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('seller_id')
    )


def downgrade():
    op.drop_table('seller')
