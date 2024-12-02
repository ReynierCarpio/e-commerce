"""empty message

Revision ID: d0e79061d439
Revises: c9d79061d438
Create Date: 2024-12-02 01:22:10
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0e79061d439'
down_revision = 'c9d79061d438'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('user',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('address', sa.String(length=255), nullable=False),
    sa.Column('phone_number', sa.String(length=15), nullable=False),
    sa.Column('role', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email')
    )


def downgrade():
    op.drop_table('user')
