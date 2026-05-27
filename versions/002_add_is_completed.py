"""add is_completed to goals

Revision ID: 002
Revises: 001
Create Date: 2026-05-27
"""
from alembic import op
import sqlalchemy as sa

revision = '002'
down_revision = '001'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('goals', sa.Column('is_completed', sa.SmallInteger(), nullable=False, server_default='0'))


def downgrade():
    op.drop_column('goals', 'is_completed')
