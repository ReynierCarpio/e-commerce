"""empty message

Revision ID: a7b79061d436
Revises:
Create Date: 2024-12-02 01:03:57.851524
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a7b79061d436'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('admin',
    sa.Column('admin_id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('admin_id')
    )


def downgrade():
    op.drop_table('admin')
