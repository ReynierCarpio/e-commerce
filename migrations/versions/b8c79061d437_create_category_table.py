"""empty message

Revision ID: b8c79061d437
Revises: a7b79061d436
Create Date: 2024-12-02 01:15:00
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8c79061d437'
down_revision = 'a7b79061d436'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('category',
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('category_name', sa.String(length=255), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('category_id')
    )


def downgrade():
    op.drop_table('category')
